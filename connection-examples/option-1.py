# Using Socket Programming Directly

# Basic example of how to connect and communicate with your server:

import socket

def send_command(command, host='127.0.0.1', port=6380):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(command.encode('utf-8'))
    
    response = client.recv(4096).decode('utf-8')
    client.close()
    
    return response

if __name__ == "__main__":
    # Example usage
    response = send_command("SET mykey myvalue")
    print(f"Response: {response}")
    
    response = send_command("GET mykey")
    print(f"Response: {response}")
