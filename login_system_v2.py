import hashlib
import json
import os

USERS_FILE = "users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    users = load_users()
    if username in users:
        print("❌ Username already exists!")
        return
    users[username] = hash_password(password)
    save_users(users)
    print("✅ Account created successfully!")

def login(username, password):
    users = load_users()
    if username not in users:
        print("❌ Username not found!")
        return
    if users[username] == hash_password(password):
        print(f"✅ Welcome {username}!")
    else:
        print("❌ Invalid password!")

print("1. Register")
print("2. Login")
choice = input("Choose: ")
username = input("Enter username: ")
password = input("Enter password: ")

if choice == "1":
    register(username, password)
elif choice == "2":
    login(username, password)
