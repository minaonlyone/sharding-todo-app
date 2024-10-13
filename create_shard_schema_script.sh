#!/bin/bash

# Script to create a to-do list schema in each shard automatically

docker exec -it $(docker ps --filter "name=shard1" --format "{{.Names}}") psql -U shard_user -d todo_$(docker ps --filter "name=shard1" --format "{{.Names}}") -c "CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    description TEXT NOT NULL
);"

docker exec -it $(docker ps --filter "name=shard2" --format "{{.Names}}") psql -U shard_user -d todo_$(docker ps --filter "name=shard2" --format "{{.Names}}") -c "CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    description TEXT NOT NULL
);"

docker exec -it $(docker ps --filter "name=shard3" --format "{{.Names}}") psql -U shard_user -d todo_$(docker ps --filter "name=shard3" --format "{{.Names}}") -c "CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    description TEXT NOT NULL
);"

echo "Schema created in all shards."