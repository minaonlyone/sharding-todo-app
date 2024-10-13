# Sharding To-Do App Example

This repository provides an example of how to use database sharding with PostgreSQL, using Docker and a simple to-do list API built with Python.

## Features
- **Horizontal Sharding**: Data is distributed across multiple shards based on user ID.
- **3 PostgreSQL Shards**: Automatically created using Docker Compose.

## Getting Started

### Prerequisites
- Docker
- Python 3.x

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/minaonlyopne/sharding-todo-app.git
   cd sharding-todo-app
   ```
2. Run Docker Compose to create the shards:
   ```bash
   docker-compose up -d
   ```
3. Set up the schema in each shard:
   ```bash
   chmod +x create_shard_schema_script.sh
   ./create_shard_schema_script.sh
   ```
4. Install Python dependencies:
   ```bash
   pip install -r api/requirements.txt
   ```
5. Run the API:
   ```bash
   python api/app.py
   ```

## Testing

### Running Unit Tests
This repository includes unit tests to verify the correct functioning of the sharding and API. To run the tests, follow these steps:

1. Make sure the Docker containers are running:
   ```bash
   docker-compose up -d
   ```
2. Run the unit tests:
   ```bash
   python test_app.py
   ```

### Testing API Endpoints Manually
To add a to-do:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"user_id": 1, "description": "Buy milk"}' http://localhost:5000/todo
```

To retrieve to-dos for a user:
```bash
curl -X GET http://localhost:5000/todo/1
```

To update a to-do:
```bash
curl -X PUT -H "Content-Type: application/json" -d '{"user_id": 1, "description": "Buy almond milk"}' http://localhost:5000/todo/1
```

To delete a to-do:
```bash
curl -X DELETE -H "Content-Type: application/json" -d '{"user_id": 1}' http://localhost:5000/todo/1
```

## Sharding Strategy
This project uses horizontal sharding based on `user_id` to distribute tasks across three PostgreSQL shards. The sharding key is `user_id`, which determines the shard to which a to-do item belongs.

The benefit of sharding is that it allows the database to scale horizontally by distributing the data across multiple nodes, thereby improving performance and reliability.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

## Technologies Used
- **unittest**: Python's standard library for writing and running unit tests.
- **Python**: Backend development using Flask.
- **PostgreSQL**: Database for storing to-do items, distributed across shards.
- **Docker**: Containerization of the PostgreSQL shards.
- **Docker Compose**: To easily manage multiple containers for the sharding setup.
- **cURL**: For testing API endpoints manually.

## To-Do (Features Planned for the Future)
- **Implement Additional Sharding Strategies**: Explore different sharding strategies such as consistent hashing.
- **Dockerize the API**: Create a Docker image for the Python API to make deployment easier.

## Credits
- Developed by [Mina Adel](https://github.com/minaonlyone).