
import json
userlists=[]
USER_FILE = "users.json"
def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)
def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] 

  