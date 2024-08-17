# Redis Clone - Python

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
    git clone https://github.com/Himalayagup/redis_clone_python.git
    cd my_redis_clone
    ```

2. **Install Dependencies**

    Ensure you have Python 3 installed. Install the package locally:

    ```bash
    pip install .
    ```
    
    Alternatively, for development mode (editable install):

    ```bash
    pip install e .
    ```


## Usage

### Start the Server

To start the server with default settings (without key persistency):

```bash
redis-clone
```

To specify the host and port:

```bash
redis-clone --host 127.0.0.1 --port 6379
```

To enable key persistency (saves data to store.json and loads on restart):

```bash
redis-clone --persist
```

To enter CLI mode if server is running:


```bash
redis-clone --cli
```

## Available Commands

- `SET <key> <value>`: Sets the value for the key.
- `GET <key>`: Retrieves the value for the key. Returns (nil) if not found.
- `DEL <key>`: Deletes the key. Returns 1 if deleted, 0 if not found.
- `EXPIRE <key> <timeout>`: Sets expiration time for the key.
- `STOP`: Shuts down the server.
- `EXIT`: Exits CLI mode.

## Key Persistency
To enable key persistency, use the `--persistent` flag when starting the server. This saves data to store.json and loads it upon restart, allowing data to be retained between server restarts.

## Example Clients
Three example clients are provided (in connection-example folder) to demonstrate how to connect to the server from different environments:

- JavaScript: `js-example.js`
- Python (Simple): `option-1.py`
- Python (Custom Redis Client): `option-2.py`

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.