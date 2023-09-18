# Ask SQL Chatbot

The Ask SQL is a project that utilizes OpenAI's natural language processing capabilities to translate user-generated 
questions into SQL queries. This project aims to simplify the process of querying databases by allowing users to express
their questions in plain language, which is then converted into a structured SQL query based on the database schema,
which is directly connected to the chatbot.

![asksql](https://github.com/felipeall/ask-sql-chatbot/assets/20917430/33bd78af-3c8c-4dc7-8083-6c4441f9010e)

## Prerequisites

- Docker
- OpenAI API key

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/felipeall/ask-sql-chatbot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ask-sql-chatbot
    ```

3. Create a `.env` file
    ```bash
    cd .env.example .env
    ```

4. Set up the OpenAI API Key in the `.env` file
    ```
    OPENAI_API_KEY=..................
    ```

5. Write a database DDL query in the `docker/init.sql` file to simulate your database if it doesn't exist. E.g.:
    ```sql
    CREATE TABLE IF NOT EXISTS users (
      id UUID PRIMARY KEY NULL DEFAULT gen_random_uuid(),
      "name" TEXT NOT NULL,
      handle TEXT NOT NULL,
      created_at TIMESTAMP NOT NULL DEFAULT NOW(),
      updated_at TIMESTAMP NOT NULL DEFAULT NOW()
    );
    
    CREATE TABLE IF NOT EXISTS locations (
      id UUID PRIMARY KEY NULL DEFAULT GEN_RANDOM_UUID(),
      latitude FLOAT NOT NULL,
      longitude FLOAT NOT NULL
    );
    
    CREATE TABLE IF NOT EXISTS tweets (
      id UUID PRIMARY KEY NULL DEFAULT GEN_RANDOM_UUID(),
      created_at TIMESTAMP NOT NULL DEFAULT NOW(),
      "text" TEXT NOT NULL,
      "owner" UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      "location" UUID NOT NULL REFERENCES locations(id) ON DELETE CASCADE
    );
    ```

6. Build and run the Docker containers
    ```bash
    docker compose up -d --build
    ```

The chatbot will be available at `http://localhost:7860`
