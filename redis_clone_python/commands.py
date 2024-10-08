import time
from .utils import lock, shutdown_flag

try:
    from .utils import store, expiry_store
except:
    # Default to empty store if import fails
    store = {}
    expiry_store = {}

def execute_command(command):
    """
    Executes the given command by dispatching it to the appropriate handler.
    
    Args:
        command (list): The command and its arguments as a list of strings.
    
    Returns:
        str: The response to the command.
    """
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
    elif cmd == "PING":
        return ping_command(command)
    elif cmd == "STOP":
        shutdown_flag.set()
        return "Server is shutting down..."
    else:
        return "ERROR: Unknown command"

def set_command(command):
    """
    Sets a key-value pair in the store.
    
    Args:
        command (list): The command and its arguments as a list of strings.
    
    Returns:
        str: The response to the command.
    """
    if len(command) < 3:
        return "ERROR: SET command requires key and value"
    
    key = command[1]
    value = command[2]
    
    with lock:
        store[key] = value
    return "OK"

def get_command(command):
    """
    Retrieves the value for a given key from the store.
    
    Args:
        command (list): The command and its arguments as a list of strings.
    
    Returns:
        str: The value for the key or None if the key does not exist or has expired.
    """
    if len(command) < 2:
        return "ERROR: GET command requires a key"
    
    key = command[1]
    
    with lock:
        if key in store:
            if key in expiry_store and expiry_store[key] < time.time():
                del store[key]
                del expiry_store[key]
                return None
            return store[key] if store[key] else None
        else:
            return None

def del_command(command):
    """
    Deletes a key from the store.
    
    Args:
        command (list): The command and its arguments as a list of strings.
    
    Returns:
        str: "1" if the key was deleted, "0" if the key did not exist.
    """
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
    """
    Sets an expiration time for a key.
    
    Args:
        command (list): The command and its arguments as a list of strings.
    
    Returns:
        str: "1" if the expiration was set, "0" if the key did not exist.
    """
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

def ping_command(command):
    """
    Responds to a PING command with PONG.
    
    Args:
        command (list): The command and its arguments as a list of strings.
    
    Returns:
        str: "PONG"
    """
    return "PONG"