import socket
import threading
import time
import argparse
import sys

# In-memory store
store = {}

# Expiry data store
expiry_store = {}

# Lock for thread safety
lock = threading.Lock()

def handle_client(client_socket):
    while True:
        try:
            request = client_socket.recv(1024).decode('utf-8').strip()
            if not request:
                break
            
            command = request.split()
            response = execute_command(command)
            
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            client_socket.send(f"Error: {str(e)}".encode('utf-8'))
            break
    client_socket.close()

def execute_command(command):
    if not command:
        return "ERROR: Empty command"
    
    cmd = command[0].upper()
    
    if cmd == "SET":
        return set_command(command)
    elif cmd == "GET":
        return get_command(command)
    elif cmd == "DEL":
        return del_command(command)
    elif cmd == "EXPIRE":
        return expire_command(command)
    else:
        return "ERROR: Unknown command"

def set_command(command):
    if len(command) < 3:
        return "ERROR: SET command requires key and value"
    
    key = command[1]
    value = command[2]
    
    with lock:
        store[key] = value
    return "OK"

def get_command(command):
    if len(command) < 2:
        return "ERROR: GET command requires a key"
    
    key = command[1]
    
    with lock:
        if key in store:
            if key in expiry_store and expiry_store[key] < time.time():
                del store[key]
                del expiry_store[key]
                return "nil"
            return store[key]
        else:
            return "nil"

def del_command(command):
    if len(command) < 2:
        return "ERROR: DEL command requires a key"
    
    key = command[1]
    
    with lock:
        if key in store:
            del store[key]
            if key in expiry_store:
                del expiry_store[key]
            return "1"
        else:
            return "0"

def expire_command(command):
    if len(command) < 3:
        return "ERROR: EXPIRE command requires a key and timeout"
    
    key = command[1]
    timeout = int(command[2])
    
    with lock:
        if key in store:
            expiry_store[key] = time.time() + timeout
            return "1"
        else:
            return "0"

def start_server(host, port):
    while True:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((host, port))
            server.listen(5)
            print(f"Server listening on {host}:{port}")
            
            while True:
                client_socket, addr = server.accept()
                client_handler = threading.Thread(target=handle_client, args=(client_socket,))
                client_handler.start()
        
        except Exception as e:
            print(f"Server error: {e}. Restarting in 5 seconds...")
            time.sleep(5)

def main():
    parser = argparse.ArgumentParser(description="Start a Redis-like server")
    parser.add_argument('--host', default="0.0.0.0", help="Host to bind the server")
    parser.add_argument('--port', type=int, default=6379, help="Port to bind the server")
 
    args = parser.parse_args()
 
    start_server(args.host, args.port)

if __name__ == "__main__":
    main()
