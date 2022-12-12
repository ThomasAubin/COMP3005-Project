import psycopg2

def addAddress(user_username):
    # set your database details here
    hostname = 'localhost'
    database = 'look_inna_book'
    username = 'postgres'
    pwd = 'admin'
    portId = '5432'


    #connect to data base
    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = portId)

    #create a cursor for querying
    cursor = connection.cursor()


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


    #save data
    connection.commit()

    #close connections and cursor
    cursor.close()
    connection.close()



def addPayment(user_username):
    # set your database details here
    hostname = 'localhost'
    database = 'look_inna_book'
    username = 'postgres'
    pwd = 'admin'
    portId = '5432'


    #connect to data base
    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = portId)

    #create a cursor for querying
    cursor = connection.cursor()


    print("\n\n================Payment Info==============\n\n")
    cardNum = input("Card Number: ")
    expiry = input("Expiry: ")
    code = input("Security Code: ")
    fname = input("First name: ")
    lname = input("Last name: ")
   

    # Add the address to the table
    insertAddr = 'INSERT INTO paymentcards (num, expiry, digitcode3, fname, lname, user_username) VALUES (%s,%s,%s,%s,%s,%s)'
    addrValue = (cardNum, expiry, code, fname, lname, user_username) 

    cursor.execute(insertAddr, addrValue)

    #save data
    connection.commit()

    #close connections and cursor
    cursor.close()
    connection.close()

#addAddress(1)
#addPayment(1)
#addPayment("1")