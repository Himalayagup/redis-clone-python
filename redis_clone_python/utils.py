import threading
import json
import os

# In-memory store
store = {}

# Expiry data store
expiry_store = {}

# Lock for thread safety
lock = threading.Lock()

# Shutdown flag
shutdown_flag = threading.Event()

PERSISTENCE_FILE = "store.json"

def save_store():
    """
    Save the current state of the store to the persistence file.
    Uses a lock to ensure thread safety while writing to the file.
    """
    with lock:
        with open(PERSISTENCE_FILE, 'w') as f:
            json.dump(store, f)

def save_blank_store():
    """
    Save an empty dictionary to the persistence file.
    This can be used to clear the stored data.
    Uses a lock to ensure thread safety while writing to the file.
    """
    with lock:
        with open(PERSISTENCE_FILE, 'w') as f:
            json.dump({}, f)

def load_store():
    """
    Load the state of the store from the persistence file.
    If the file exists, the data is read and loaded into the store.
    If the file does not exist, the store remains empty.
    """
    global store
    if os.path.exists(PERSISTENCE_FILE):
        with open(PERSISTENCE_FILE, 'r') as f:
            store = json.load(f)
