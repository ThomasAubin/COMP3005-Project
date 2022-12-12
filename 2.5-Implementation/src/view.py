def showSplashPage():
    print("\n\n\n\n===== COMP 3005 Project =====")
    print("Students: Thomas Aubin, Jason Huynh")
    print("=============================\n\n\n\n")

    print("=============================")
    print("      Look Inna Book")
    print("     Online Bookstore\n")
    print("    \"Knowledge is power!\"")
    print("=============================")

def welcomePage():
    print("\n\nHow can we help you today?")
    print("1. Register")
    print("2. Login")
    print("3. Quit")

    return getProperInput(3)

def showHomeScreen(user):
    if (user.type == "customer"):
        print("\n\n=================  Home ================= ")
        print("Username:", user.username, "   Account Type: ", user.type)
        print("\n\n Actions")
        print("1. Add address")
        print("2. Add payment")
        print("3. Search for books")
        print("4. Make order")
        print("5. Checkout")
        print("6. Logout")
        
        return getProperInput(6)
    else:
        print("\n\n=================  Home ================= ")
        print("Username:", user.username, "   Account Type: ", user.type)
        print("\n\n Actions")
        print("1. Add book")
        print("2. Add publisher")
        print("3. Remove book")
        print("4. Generate report")
        print("5. Logout")
        
        return getProperInput(5)

def closePage():
    print("\n\nGoodbye. Come again!")




# ==================
# Helper Functions
# ==================

def getProperInput(numOptions):
    while True:
        choice = input("\n>> ")

        choice = convertStringToInt(choice)
        if type(choice) == int:
            if validateNumberChoice(numOptions, choice):
                return choice
        
        print("Bad input. Please enter again")

def convertStringToInt(n):
    try:
        n = int(n)
        return n
    except:
        return False

def validateNumberChoice(numOptions, choice):
    if choice in range(1, numOptions+1):
        return True
    else:
        return False
