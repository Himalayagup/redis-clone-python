# Using a Custom Client Library

import socket

class RedisCloneClient:
    def __init__(self, host='127.0.0.1', port=6379):
        self.host = host
        self.port = port
    
    def send_command(self, command):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, self.port))
        client.send(command.encode('utf-8'))
        
        response = client.recv(4096).decode('utf-8')
        client.close()
        
        return response
    
    def set(self, key, value):
        return self.send_command(f"SET {key} {value}")
    
    def get(self, key):
        return self.send_command(f"GET {key}")
    
    def delete(self, key):
        return self.send_command(f"DEL {key}")
    
    def expire(self, key, seconds):
        return self.send_command(f"EXPIRE {key} {seconds}")

if __name__ == "__main__":
    client = RedisCloneClient()
    print(client.set("mykey", "myvalue"))
    print(client.get("mykey"))
    print(client.delete("mykey"))
    print(client.get("mykey"))
