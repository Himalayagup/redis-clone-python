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
    with lock:
        with open(PERSISTENCE_FILE, 'w') as f:
            json.dump(store, f)

def save_blank_store():
    with lock:
        with open(PERSISTENCE_FILE, 'w') as f:
            json.dump({}, f)

def load_store():
    global store
    if os.path.exists(PERSISTENCE_FILE):
        with open(PERSISTENCE_FILE, 'r') as f:
            store = json.load(f)
