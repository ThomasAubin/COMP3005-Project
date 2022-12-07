import view

def launch():
    view.showSplashPage()

    choice = view.welcomePage()
    if (choice == 1):
        pass
        # Register
    elif (choice == 2):
        pass
        # Login
    else:
        view.closePage()
        quit()
