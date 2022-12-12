from src import view
from src import database
from src import register


def launch():
    connection = database.connect()

    view.showSplashPage()

    choice = view.welcomePage()
    if (choice == 1):
        register.register(connection)
    elif (choice == 2):
        pass
        # Login
    else:
        view.closePage()
        quit()
