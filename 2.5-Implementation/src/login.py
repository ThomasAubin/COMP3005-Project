from src.models import user

def login(connection):
    cursor = connection.cursor()

    while True:
        print("\n\n================= LOGIN =================")
        username = input("Username: ")
        password = input("Password: ")

        cursor.execute("SELECT username, fname, lname, type, password FROM users WHERE username = %s AND password = %s", (username, password))
        thisUser = cursor.fetchone()

        if thisUser is None:
            print("Sorry, there is an incorrect username or password")
        else:
            print("Login Successful")
            break

    cursor.close()

    return user.User(thisUser[0], thisUser[1], thisUser[2], thisUser[3], thisUser[4])
