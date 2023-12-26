


def addPassword(username, password):
    mp = password
    salt = generate_salt()
    salted_password = salt + mp
    hashed_password = bcrypt.hashpw(salted_password.encode(), bcrypt.gensalt()).decode()

    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords (username, hashed_password, salt) VALUES (?, ?, ?)', (username, hashed_password, salt))
    conn.commit()
    conn.close()


def getPassword(username):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('SELECT hashed_password, salt FROM passwords WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        hashed_password, salt = result
        return hashed_password, salt
    else:
        return None, None

def retrievePassword():
    username = input("Enter the username to retrieve the password: ")
    hashed_password, salt = getPassword(username)

    if hashed_password and salt:
        print("Hashed Password:", hashed_password)
        print("Salt:", salt)
    else:
        print("Username not found.")

def comparePasswords():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    hashed_password, salt = getPassword(username)

    if hashed_password and salt:
        salted_password = salt + password
        if bcrypt.checkpw(salted_password.encode(), hashed_password.encode()):
            print("Password is correct.")
        else:
            print("Password is incorrect.")
    else:
        print("Username not found.")

def getOriginalPassword():
    username = input("Enter your username: ")
    password = input("Enter your master password: ")

    hashed_password, salt = getPassword(username)

    if hashed_password and salt:
        master_key = computeMasterKey(password, salt)
        decrypted_password = decrypt(master_key, hashed_password)
        print("Original Password:", decrypted_password)
    else:
        print("Username not found.")

def main():
    createTable()

    while True:
        print("1. Store Password")
        print("2. Retrieve Password")
        print("3. Compare Passwords")
        print("4. Get Original Password")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            confirm_password = input("Retype your password: ")

            if password != confirm_password:
                print("Passwords do not match.")
                continue

            addPassword(username, password)
            print("Password stored successfully.")

        elif choice == "2":
            retrievePassword()

        elif choice == "3":
            comparePasswords()

        elif choice == "4":
            getOriginalPassword()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

main()

main()
