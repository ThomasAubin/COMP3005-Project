from src import view
from src.models import user

def register(connection):
    cursor = connection.cursor()

    while True:
        try:
            # Ask the users information and store data
            print("\n\n================User Info==============")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            username = input("Username: ")
            password = input("Password: ")
            finalType = ""

            print("Type of user 1. Customer | 2. Manager")
            type = view.getProperInput(2)

            # Set type
            if type == 1:
                finalType = "customer"
            elif type == 2:
                finalType = "manager"

            # Add the user to the table
            insertUser = 'INSERT INTO users (username, fname, lname, type, password) VALUES (%s, %s, %s, %s, %s) RETURNING username'
            userValue = (username, fname, lname, finalType, password) 

            cursor.execute(insertUser, userValue)
            userUsername = cursor.fetchone()[0]

            break

        except Exception as e:
            connection.commit() # Need to commit after an error
            print("\n\n!!! Username already exists. Please enter another username !!!")


    # ====================================


    print("\n\n================Address Info==============\n\n")
    streetNum = input("Street Number: ")
    street = input("Street Name: ")
    city = input("City: ")
    postalCode = input("Postal Code: ")
    country = input("Country: ")
    type = "home" # Put home as default
    name = input("Name of the address: ")

    # Add the address to the table
    insertAddr = 'INSERT INTO addresses (street_num, street, city, postal_code, country, type, name) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING uid'
    addrValue = (streetNum, street, city, postalCode, country, type, name) 

    cursor.execute(insertAddr, addrValue)
    addressUID = cursor.fetchone()[0]


    # ====================================


    insertUserHasAddress= 'INSERT INTO user_has_address (address_uid, user_username) VALUES (%s,%s)'
    userHasAddressValue = (addressUID, userUsername) 

    cursor.execute(insertUserHasAddress, userHasAddressValue)


    # ====================================


    connection.commit()
    cursor.close()

    print("\n\nRegistration successful")

    return user.User(username, fname, lname, type, password)
