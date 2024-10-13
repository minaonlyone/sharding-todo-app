import unittest
import requests
import psycopg2
import logging

BASE_URL = "http://localhost:5000"

# Shard connection details
shards = {
    "shard1": {"dbname": "todo_shard1", "user": "shard_user", "password": "shard_password", "host": "localhost", "port": 5433},
    "shard2": {"dbname": "todo_shard2", "user": "shard_user", "password": "shard_password", "host": "localhost", "port": 5434},
    "shard3": {"dbname": "todo_shard3", "user": "shard_user", "password": "shard_password", "host": "localhost", "port": 5435},
}

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_shard_connection(user_id):
    shard_number = user_id % len(shards)
    shard_key = f"shard{shard_number + 1}"
    logging.info(f"Connecting to shard '{shard_key}' for user_id {user_id}")
    return psycopg2.connect(**shards[shard_key])


class TestShardingLogic(unittest.TestCase):

    def setUp(self):
        # Clear todos table in each shard before tests
        logging.info("Clearing todos table in each shard before running tests.")
        for shard_name, shard in shards.items():
            conn = psycopg2.connect(**shard)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todos")
            conn.commit()
            cursor.close()
            conn.close()
            logging.info(f"Cleared todos in {shard_name}.")

    def test_add_multiple_todos_and_verify_shards(self):
        todos = [
            {"user_id": 1, "description": "To-Do for user 1"},
            {"user_id": 2, "description": "To-Do for user 2"},
            {"user_id": 3, "description": "To-Do for user 3"},
            {"user_id": 4, "description": "To-Do for user 4"},
            {"user_id": 5, "description": "To-Do for user 5"},
            {"user_id": 6, "description": "To-Do for user 6"},
        ]

        # Add multiple to-dos
        for todo in todos:
            logging.info(f"Adding to-do for user_id {todo['user_id']} with description: '{todo['description']}'")
            response = requests.post(f"{BASE_URL}/todo", json=todo)
            self.assertEqual(response.status_code, 200)
            self.assertIn("To-Do added successfully", response.json().get("message"))
            logging.info(f"Successfully added to-do for user_id {todo['user_id']}.")

        # Verify each to-do is in the correct shard
        for todo in todos:
            logging.info(f"Verifying to-do for user_id {todo['user_id']} is in the correct shard.")
            conn = get_shard_connection(todo["user_id"])
            cursor = conn.cursor()
            cursor.execute("SELECT user_id, description FROM todos WHERE user_id = %s", (todo["user_id"],))
            result = cursor.fetchone()
            cursor.close()
            conn.close()

            # Verify that we found the correct to-do in the shard
            self.assertIsNotNone(result)
            self.assertEqual(result[0], todo["user_id"])
            self.assertEqual(result[1], todo["description"])
            logging.info(f"Verified to-do for user_id {todo['user_id']} is correctly stored in the shard.")

if __name__ == '__main__':
    unittest.main()
