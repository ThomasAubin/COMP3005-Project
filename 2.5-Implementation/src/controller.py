from src import view
from src import database
from src import register
from src import login

thisUser = None
connection = None

def launch():
    global connection

    connection = database.connect()

    view.showSplashPage()

    # Run code infinitely. 
    while True:
        mainloop()

def mainloop():
    authorization()
    main()

def authorization():
    global thisUser

    while True:
        choice = view.welcomePage()
        if (choice == 1):
            thisUser = register.register(connection)
            break
        elif (choice == 2):
            thisUser = login.login(connection)
            break
        else:
            view.closePage()
            quit()

def main():
    if (thisUser.type == "customer"):
        while True:
            choice = view.showHomeScreen(thisUser)
            if (choice == 1):
                pass
            elif (choice == 2):
                pass
            elif (choice == 3):
                pass
            elif (choice == 4):
                pass
            elif (choice == 5):
                pass
            else:
                break
    else:
        while True:
            choice = view.showHomeScreen(thisUser)
            if (choice == 1):
                pass
            elif (choice == 2):
                pass
            elif (choice == 3):
                pass
            elif (choice == 4):
                pass
            else:
                break
