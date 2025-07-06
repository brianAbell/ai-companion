import json
import os

from datetime import datetime

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "..", "memory.json")


def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def add_memory_event(suggestion):
    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    if "pinned_moments" not in data:
        data["pinned_moments"] = []

    new_entry = {"summary": suggestion, "date": datetime.now().strftime("%Y-%m-%d")}

    # Avoid duplicates
    if new_entry["summary"] not in [m["summary"] for m in data["pinned_moments"]]:
        data["pinned_moments"].append(new_entry)

        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)
