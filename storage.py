import json
import os

FILE = "data.json"

def load_data():
    if not os.path.exists(FILE):
        return {"sessions": []}
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def add_session(session):
    data = load_data()
    data["sessions"].append(session)
    save_data(data)