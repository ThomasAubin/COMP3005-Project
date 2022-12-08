import psycopg2

# set your database details here
hostname = 'localhost'
database = 'Look_Inna_Book'
username = 'postgres'
pwd = 'Neverletitrun!5'
portId = '5432'

#initialise the connection and cursor
connection = None
cursor = None

try:
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
    fname = input("First Name: ")
    lname = input("Last Name: ")

    print("\n\n================Address==============\n\n")
    streetNum = input("Street Number: ")
    street = input("Street Name: ")
    city = input("City: ")
    postalCode = input("Postal Code: ")
    country = input("Country: ")
    type = "home"
    name = input("Name of the address: ")

    #create the user table if not exist
    createUser = ''' CREATE TABLE IF NOT EXISTS Users (
        UID     SERIAL PRIMARY KEY,
        fname   varchar(100) NOT NULL,
        lname   varchar(100) NOT NULL)    '''

    #create the address table if not exist
    createAddr = ''' CREATE TABLE IF NOT EXISTS Address (
        UID         SERIAL PRIMARY KEY,
        streetNum   int NOT NULL,
        street      varchar(100) NOT NULL,
        city        varchar(100) NOT NULL,
        postalCode  varchar(100) NOT NULL,
        country     varchar(100) NOT NULL,
        type        varchar(100) NOT NULL,
        name        varchar(100) NOT NULL)    '''

    insertUser = 'INSERT INTO Users (UID, fname, lname) VALUES (%s, %s, %s)'
    userValue = (1, fname, lname)

    insertAddr = 'INSERT INTO Address (UID, streetNum, street, city, postalCode, country, type, name'
    addrValue = (1, streetNum, street, city, postalCode, country, type, name)

    
    #exectute commands
    cursor.execute(createUser)
    cursor.execute(createAddr)








    #save the new things to the database
    connection.commit()




    #close connections and cursor
    cursor.close()
    connection.close()

#error handling
except Exception as error:
    print(error)
finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()