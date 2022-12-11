import psycopg2

def register():
    # set your database details here
    hostname = 'localhost'
    database = 'Look_Inna_Book'
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



    #asks for the users information and stores data
    print("\n\n================User Info==============\n\n")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    username = input("Username: ")
    password = input("Password: ")
    finalType = ""

    while True:
        type = input("Type of user 1. Customer | 2. Manager: ")
        if int(type) == 1 or int(type) == 2:
            break
        else:
            print("\nPlease type '1' for Customer or '2' for Manager")
            continue
    

    #set type
    if type == 1:
        finalType = "customer"
    elif type == 2:
        finalType = "manager"


    print("\n\n================Address Info==============\n\n")
    streetNum = input("Street Number: ")
    street = input("Street Name: ")
    city = input("City: ")
    postalCode = input("Postal Code: ")
    country = input("Country: ")
    type = "home" #put home as default
    name = input("Name of the address: ")


    #adding the user to the table
    insertUser = 'INSERT INTO users (username, fname, lname, type, password) VALUES (%s, %s, %s, %s, %s)'
    userValue = (username, fname, lname, finalType, password) 

    #adding the address to the table
    insertAddr = 'INSERT INTO addresses (streetNum, street, city, postal_code, country, type, name) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING uid'
    addrValue = (streetNum, street, city, postalCode, country, type, name) 

    #exectute commands
    cursor.execute(insertUser, userValue)

    cursor.execute(insertAddr, addrValue)
    addrId = cursor.fetchone()

    #check to make sure added MUST CHANGE TO UID******
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    addUser = cursor.fetchone()

    #check to make sure added MUST CHANGE TO UID******
    cursor.execute("SELECT * FROM address WHERE uid = %s", (addrId,))
    addAddress = cursor.fetchone()

    if addUser is not None and addAddress is not None:
        print("Registration successful")

    #save the new things to the database
    connection.commit()

    #close connections and cursor
    cursor.close()
    connection.close()


# register()