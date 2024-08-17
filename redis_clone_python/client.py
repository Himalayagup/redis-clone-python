import socket

def send_command(command, host, port):
    """
    Sends a command to the server and receives the response.
    
    Args:
        command (str): The command to send to the server.
        host (str): The hostname or IP address of the server.
        port (int): The port number to connect to on the server.
    
    Returns:
        str: The server's response to the command, or an error message if an exception occurs.
    """
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        client.send(command.encode('utf-8'))
        
        response = client.recv(4096).decode('utf-8')
        client.close()
        
        return response
    except OSError as e:
        return f"Error: {e}"
