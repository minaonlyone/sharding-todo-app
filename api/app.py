from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Define connection details for shards
shards = {
    "shard1": {"dbname": "todo_shard1", "user": "shard_user", "password": "shard_password", "host": "localhost", "port": 5433},
    "shard2": {"dbname": "todo_shard2", "user": "shard_user", "password": "shard_password", "host": "localhost", "port": 5434},
    "shard3": {"dbname": "todo_shard3", "user": "shard_user", "password": "shard_password", "host": "localhost", "port": 5435},
}

# Function to determine shard based on user ID
def get_shard(user_id):
    shard_number = user_id % len(shards)
    shard_key = f"shard{shard_number + 1}"
    return psycopg2.connect(**shards[shard_key])

@app.route('/todo', methods=['POST'])
def add_todo():
    data = request.json
    user_id = data.get('user_id')
    description = data.get('description')

    conn = get_shard(user_id)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (user_id, description) VALUES (%s, %s)", (user_id, description))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "To-Do added successfully!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
