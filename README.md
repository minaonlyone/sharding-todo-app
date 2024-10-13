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
2. Run Docker Compose to create the shards:

    ```bash
    docker-compose up -d
3. Set up the schema in each shard:

4. Install Python dependencies:
    ```bash
    pip install -r api/requirements.txt
5. Run the API:
    ```bash
    python api/app.py

## Testing
To add a to-do:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"user_id": 1, "description": "Buy milk"}' http://localhost:5000/todo

## Sharding Strategy
This project uses horizontal sharding based on user_id to distribute tasks across three PostgreSQL shards. The sharding key is user_id, which determines the shard to which a to-do item belongs.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.


