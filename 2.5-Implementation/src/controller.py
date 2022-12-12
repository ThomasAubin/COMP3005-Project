from src import view
from src import database
from src import register
from src import login

username = ""

def launch():
    connection = database.connect()

    view.showSplashPage()

    choice = view.welcomePage()
    if (choice == 1):
        username = register.register(connection)
    elif (choice == 2):
        username = login.login(connection)
    else:
        view.closePage()
        quit()

    print(username)
