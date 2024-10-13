#!/bin/bash

# Script to create a to-do list schema in each shard automatically

# Create the to-do list schema in each shard
echo "Creating schema in shard1..."
docker exec -i $(docker ps --filter "name=shard1" --format "{{.Names}}") psql -U shard_user -d todo_shard1 -c "CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    description TEXT NOT NULL
);" && echo "Schema created successfully in shard1" || echo "Failed to create schema in shard1"

echo "Creating schema in shard2..."
docker exec -i $(docker ps --filter "name=shard2" --format "{{.Names}}") psql -U shard_user -d todo_shard2 -c "CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    description TEXT NOT NULL
);" && echo "Schema created successfully in shard2" || echo "Failed to create schema in shard2"

echo "Creating schema in shard3..."
docker exec -i $(docker ps --filter "name=shard3" --format "{{.Names}}") psql -U shard_user -d todo_shard3 -c "CREATE TABLE todos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    description TEXT NOT NULL
);" && echo "Schema created successfully in shard3" || echo "Failed to create schema in shard3"

echo "Schema created in all shards."
