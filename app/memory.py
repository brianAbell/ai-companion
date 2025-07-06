import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "..", "memory.json")

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)
