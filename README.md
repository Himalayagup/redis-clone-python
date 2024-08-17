# My Redis Clone

## Overview

`my_redis_clone` is a simple Redis-like server written in Python. It supports basic commands such as `SET`, `GET`, `DEL`, `EXPIRE`, and `STOP`. The server can be run with optional key persistency using a JSON file. 

## Features

- **Basic Commands**: Implements basic Redis commands including `SET`, `GET`, `DEL`, and `EXPIRE`.
- **Persistency**: Optionally supports key persistency by saving and loading data from a JSON file.
- **Multi-threaded**: Handles multiple client connections using threads.
- **CLI Mode**: Provides a command-line interface for interacting with the server.

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/my_redis_clone.git
    cd my_redis_clone
    ```

2. **Install Dependencies**

    Ensure you have Python 3 installed. Install the package locally:

    ```bash
    pip install .
    ```

## Usage

### Start the Server

To start the server without key persistency:

```bash
redis-clone
```

To start the server on specific IP and PORT:

```bash
redis-clone --host 127.0.0.1 --port 6379
```

With key persistency:

```bash
redis-clone --persist
```

To use CLI mode:


```bash
redis-clone --cli
```

## Available Commands

- `SET <key> <value>`: Sets the value for the key.
- `GET <key>`: Retrieves the value for the key. Returns (nil) if not found.
- `DEL <key>`: Deletes the key. Returns 1 if deleted, 0 if not found.
- `EXPIRE <key> <timeout>`: Sets expiration time for the key.
- `STOP`: Shuts down the server.
- `EXIT`: Exits the CLI.

## Key Persistency
Enable key persistency with the --persist flag. It saves data to store.json and loads it on restart.