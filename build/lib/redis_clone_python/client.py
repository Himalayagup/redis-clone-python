import socket

def send_command(command, host, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        client.send(command.encode('utf-8'))
        
        response = client.recv(4096).decode('utf-8')
        client.close()
        
        return response
    except OSError as e:
        return f"Error: {e}"
