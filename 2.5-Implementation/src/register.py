import psycopg2

def register():
    # set your database details here
    hostname = 'localhost'
    database = 'Look_Inna_Book'
    username = 'postgres'
    pwd = 'Neverletitrun!5'
    portId = '5432'

    #initialise the connection and cursor
    connection = None
    cursor = None

#    try:
    #connect to data base
    connection = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = portId)
    
    #create a cursor for querying
    cursor = connection.cursor()



    #asks for the users information and stores data
    print("\n\n================User Info==============\n\n")
    fname = input("First Name: ")
    lname = input("Last Name: ")

    print("\n\n================Address Info==============\n\n")
    streetNum = input("Street Number: ")
    street = input("Street Name: ")
    city = input("City: ")
    postalCode = input("Postal Code: ")
    country = input("Country: ")
    type = "home" #put home as default
    name = input("Name of the address: ")


    #adding the user to the table
    insertUser = 'INSERT INTO Users (UID, fname, lname) VALUES (%s, %s, %s)'
    userValue = (2, fname, lname) #dont know what to put for UID

    #adding the address to the table
    insertAddr = 'INSERT INTO Address (UID, streetNum, street, city, postalCode, country, type, name) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
    addrValue = (2, streetNum, street, city, postalCode, country, type, name) #dont know what to put for UID

    #exectute commands
    cursor.execute(insertUser, userValue)
    cursor.execute(insertAddr, addrValue)

    #check to make sure added MUST CHANGE TO UID******
    cursor.execute("SELECT * FROM users WHERE fname = %s", (fname,))
    addUser = cursor.fetchone()

    #check to make sure added MUST CHANGE TO UID******
    cursor.execute("SELECT * FROM address WHERE street = %s", (street,))
    addAddress = cursor.fetchone()

    if addUser is not None and addAddress is not None:
        print("Registration successful")

    #save the new things to the database
    connection.commit()

    #close connections and cursor
    cursor.close()
    connection.close()

    # #error handling
    # except Exception as error:
    #     print(error)
    # finally:
    #     if cursor is not None:
    #         cursor.close()
    #     if connection is not None:
    #         connection.close()

register()