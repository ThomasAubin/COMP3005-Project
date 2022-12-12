from src import view
from src import database


def launch():
    connection = database.connect()

    view.showSplashPage()

    choice = view.welcomePage()
    if (choice == 1):
        pass
    elif (choice == 2):
        pass
        # Login
    else:
        view.closePage()
        quit()
