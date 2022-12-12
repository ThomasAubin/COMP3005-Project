from src import view
from src import database
from src import register
from src import login
from src import userFunctions
from src import makeOrder
from src import checkout
from src import ownerOperations
from src import search

thisUser = None
connection = None
order = []

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
    global order

    if (thisUser.type == "customer"):
        while True:
            choice = view.showHomeScreen(thisUser)
            if (choice == 1):
                userFunctions.addAddress(connection, thisUser)
            elif (choice == 2):
                userFunctions.addPayment(connection, thisUser)
            elif (choice == 3):
                search.search(connection)
            elif (choice == 4):
                order = makeOrder.makeOrder(connection)
            elif (choice == 5):
                checkout.checkout(connection, thisUser, order)
            else:
                break
    else:
        while True:
            choice = view.showHomeScreen(thisUser)
            if (choice == 1):
                ownerOperations.addBook(connection)
            elif (choice == 2):
                ownerOperations.addPub(connection)
            elif (choice == 3):
                ownerOperations.addAuth(connection)
            elif (choice == 4):
                ownerOperations.removeBook(connection)
            elif (choice == 5):
                pass
            else:
                break
