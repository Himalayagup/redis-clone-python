import argparse
from .server import start_server
from .client import send_command

def cli_mode(host, port):
    """
    Runs the command-line interface (CLI) mode for interacting with the server.
    Users can enter commands to interact with the server and type 'exit' to quit CLI mode.
    
    Args:
        host (str): The host address of the server.
        port (int): The port number on which the server is listening.
    """

    print("Entering CLI mode. Type your commands or 'exit' to quit.")
    
    while True:
        command = input("redis-clone> ").strip()
        if command.lower() == "exit":
            print("Exiting CLI mode. You can reconnect by using the '--cli' option.")
            break
        
        response = send_command(command, host, port)
        if response is None:
            print("(nil)")
        else:
            print(response)
        
        if command.upper() == "STOP":
            print("Server is shutting down. Exiting CLI.")
            break

def main():
    """
    Parses command-line arguments and starts the server or CLI mode based on the arguments.
    The server can be started with or without persistence and the CLI mode can be enabled.
    """
    parser = argparse.ArgumentParser(description="Start a Redis-like server with CLI")
    parser.add_argument('--host', default="127.0.0.1", help="Host to bind the server")
    parser.add_argument('--port', type=int, default=6379, help="Port to bind the server")
    parser.add_argument('--cli', action='store_true', help="Run in CLI mode")
    parser.add_argument('--persistent', action='store_true', help="Enable key persistence")

    args = parser.parse_args()

    if args.cli:
        cli_mode(args.host, args.port)
    else:
        from threading import Thread
        server_thread = Thread(target=start_server, args=(args.host, args.port, args.persistent))
        server_thread.start()

        # Start CLI mode immediately after starting the server
        cli_mode(args.host, args.port)
        server_thread.join()

if __name__ == "__main__":
    main()
