import psycopg2



def addBook():
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

    #get the book data
    print("Lets start adding a book!")
    isbn = input("What is the isbn of the book: ")
    name = input("What is the title of the book: ")
    pages = input("How many pages are in the book: ")
    price = input("What is the price of the book: ")
    quantity = input("How many of these books do you have in stock: ")
    percent = input("What is the publisher percentage: ")
    email = input("What is the publisher's email: ")

    #add the book
    print("Adding book...")
    cursor.execute("INSERT INTO Books(ISBN, name, pages, price, quantity, publisher_share_percentage, publisher_email) VALUES (%s, %s, %s, %s, %s, %s, %s)", (isbn, name, pages, float(price), int(quantity), int(percent), email))

    #make sure it added
    cursor.execute("SELECT * FROM Books WHERE ISBN = %s", (isbn,))
    if cursor.fetchone() is not None:
        print("Add successful")


    #save data
    connection.commit()

    #close connections and cursor
    cursor.close()
    connection.close()



def removeBook():
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

    #get book isbn
    isbn = input("What is the ISBN for the book you want to delete? ")
    print("Okay, deleting now...")

    #make sure book exists
    cursor.execute("SELECT * FROM Books WHERE ISBN = %s", (isbn,))

    if cursor.fetchone() is not None:
        #delete book
        cursor.execute("DELETE FROM Books WHERE ISBN = %s", (isbn,))
        print("Deletion complete")
    
    #if book doesnt exist
    else:
        print("Sorry, a book with that ISBN does not exist")
        while True:
            userIn = input("Would you like to delete something else? (y/n)")
            if userIn == "y" or userIn == "Y":
                removeBook()
                return
            elif userIn == "n" or userIn == "N":
                return
            else:
                print("Sorry that was an invalid input, please type 'y' for yes or 'n' for no")
    #save data
    connection.commit()

    #close connections and cursor
    cursor.close()
    connection.close()

# addBook()
