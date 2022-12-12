from src import view
from src import database
from src import register
from src import login
from src.models import user

thisUser = None

def launch():
    connection = database.connect()

    view.showSplashPage()

    choice = view.welcomePage()
    if (choice == 1):
        thisUser = register.register(connection)
    elif (choice == 2):
        thisUser = login.login(connection)
    else:
        view.closePage()
        quit()
