import hashlib
import random
import string
import sqlite3
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
import bcrypt
from cryptography.fernet import Fernet


def createTables():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            masterkey_hash TEXT,
            device_secret TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            password TEXT,
            app_name TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS secrets (
            masterkey_hash TEXT NOT NULL,
            device_secret TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def encrypt(key, source):
    f = Fernet(key)
    encrypted_data = f.encrypt(source.encode())
    return encrypted_data.decode()

def decrypt(key, source):
    f = Fernet(key)
    decrypted_data = f.decrypt(source.encode())
    return decrypted_data.decode()

def register():
    username = input("Enter your username: ")
    password = input("Enter your master password: ")
    hashed_master = hashlib.sha512(password.encode()).hexdigest()
    secret = ''.join(random.choice(string.ascii_letters) for i in range(16))

    query = "INSERT INTO users (username, masterkey_hash, device_secret) VALUES (?, ?, ?)"
    values = (username, hashed_master, secret)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    conn.close()

def compute_master_key(masterpass, device_secret):
    password = masterpass.encode()
    salt = device_secret.encode()
    key = PBKDF2(password, salt, dkLen=32, count=1000000, hmac_hash_module=SHA512)
    return key

def get_device_secret(username):
    query = "SELECT device_secret FROM users WHERE username = ?"
    values = (username,)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute(query, values)
    result = cursor.fetchone()
    conn.close()
    return result[0]

def get_masterkey_hash(username):
    query = "SELECT masterkey_hash FROM users WHERE username = ?"
    values = (username,)
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute(query, values)
    result = cursor.fetchone()
    conn.close()
    return result[0]

## add.py
def add_entry(masterpass, device_secret, user_id):
    ds = device_secret
    password = masterpass
    master_key = compute_master_key(masterpass, ds)
    encrypted_password = encrypt(master_key, password)
    query = "INSERT INTO passwords (user_id, password, app_name) VALUES (?, ?, ?)"
    values = (user_id, encrypted_password, "Facebook")
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    conn.close()


def get_entries(masterpass, device_secret, hashed_master):
    master_key = compute_master_key(masterpass, device_secret)
    decrypted_password = decrypt(master_key, hashed_master)
    password = decrypted_password.decode()



def login():
    # OK
    username = input("Enter your username: ")
    password = input("Enter your master password: ")
    hashed_master = get_masterkey_hash(username)
    given_hash = hashlib.sha512(password.encode()).hexdigest()
    if given_hash == hashed_master:
        print("Login successful.")
        mp = password
        DS = get_device_secret(username)
        return(mp, DS)
    else:
        print("Password is incorrect.")

def main():
    mp = None
    ds = None
    CURRENT_USER_ID = 1
    createTables()

    while True:
        result = input("1. Login\n2. Register\n3. Add password\n4. Get password\n")
        if result == "1":
            mp, ds = login()
            print("mp: ", mp)
            print("ds: ", ds)
        elif result == "2":
            register()
        elif result == "3":
            add_entry(mp, ds, CURRENT_USER_ID)
        else:
            print("Invalid input.")

main()