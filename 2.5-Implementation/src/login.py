def login(connection):
    cursor = connection.cursor()

    username = ""

    while True:
        print("\n\n================= LOGIN =================")
        username = input("Username: ")
        password = input("Password: ")

        cursor.execute("SELECT username FROM users WHERE username = %s AND password = %s", (username, password))
        username = cursor.fetchone()

        if username is None:
            print("Sorry, there is an incorrect username or password")
        else:
            print("Login Successful")
            break

    cursor.close()

    return username[0]
