def addAddress(connection, user):
    user_username = user.username

    cursor = connection.cursor()


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
    userHasAddressValue = (addressUID, user_username) 

    cursor.execute(insertUserHasAddress, userHasAddressValue)


    # ====================================


    connection.commit()
    cursor.close()


def addPayment(connection, user):
    user_username = user.username

    cursor = connection.cursor()


    # ====================================


    print("\n\n================Payment Info==============\n\n")
    cardNum = input("Card Number: ")
    expiry = input("Expiry: ")
    code = input("Security Code: ")
    fname = input("First name: ")
    lname = input("Last name: ")
   

   # ====================================


    # Add the address to the table
    insertAddr = 'INSERT INTO paymentcards (num, expiry, digit_code_3, fname, lname, user_username) VALUES (%s,%s,%s,%s,%s,%s)'
    addrValue = (cardNum, expiry, code, fname, lname, user_username) 

    cursor.execute(insertAddr, addrValue)


    # ====================================


    connection.commit()
    cursor.close()
