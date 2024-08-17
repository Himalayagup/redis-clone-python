import argparse
from .server import start_server
from .client import send_command

def cli_mode(host, port):
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
