import socket
import threading
import time
from .commands import execute_command
from .utils import shutdown_flag, load_store, save_store, save_blank_store

def handle_client(client_socket):
    """
    Handles communication with a connected client.
    Receives commands from the client, executes them, and sends responses back.
    Stops handling if the client sends an empty request or if a STOP command is received.
    
    Args:
        client_socket (socket.socket): The client socket for communication.
    """
    while True:
        try:
            request = client_socket.recv(1024).decode('utf-8').strip()
            if not request:
                break
            
            command = request.split()
            response = execute_command(command)
            if response:
                client_socket.send(response.encode('utf-8'))
            else:
                client_socket.send(b"(nil)")
            
            if command[0].upper() == "STOP":
                break
        except Exception as e:
            client_socket.send(f"Error: {str(e)}".encode('utf-8'))
            break
    client_socket.close()

def start_server(host, port, persistent):
    """
    Starts the server, binds it to the given host and port, and listens for incoming client connections.
    Handles each client in a separate thread and performs persistence operations based on the 'persistent' flag.
    
    Args:
        host (str): The host to bind the server to.
        port (int): The port to bind the server to.
        persistent (bool): Whether to enable data persistence. If True, store data is saved to file upon shutdown.
    """
    # Load store data to initialize persistence data if it exists
    load_store()
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    try:
        while not shutdown_flag.is_set():
            client_socket, addr = server.accept()
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except Exception as e:
        print(f"Server error: {e}. Restarting in 5 seconds...")
        time.sleep(5)
    finally:
        # Save store data if persistence is enabled; otherwise, clear the store
        if persistent:
            save_store()
        else:
            save_blank_store()
        server.close()
        print("Server shutdown complete.")
