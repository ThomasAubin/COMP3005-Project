import psycopg2


def addPub(connection):
    cursor = connection.cursor()

    print("===============Add a publisher===========")
    email = input("What is the publisher email: ")
    pubname = input("What is the publisher name: ")
    bankNum = input("What is the publisher bank number: ")

    streetNum = input("What is the publisher street number: ")
    street = input("What is the publisher street name: ")
    city = input("What is the publisher city: ")
    postalCode = input("What is the publisher postal code: ")
    country = input("What is the publisher country: ")
    type = "home"
    name = input("What do you want to name this address: ")


    cursor.execute("INSERT INTO addresses (street_num, street, city, postal_code, country, type, name) VALUES (%s, %s, %s, %s,%s, %s,%s) RETURNING uid", (streetNum, street, city, postalCode, country, type, name))
    temp = cursor.fetchone()
    uid = temp[0]

    cursor.execute("INSERT INTO publishers (email, name, bank_num, address_uid) VALUES (%s, %s, %s, %s)", (email, pubname, bankNum, uid))
    cursor.execute("SELECT email FROM publishers WHERE email = %s", (email,))

    if cursor.fetchone() is not None:
        print("Publisher added")

    connection.commit()
    cursor.close()


def addAuth(connection):
    cursor = connection.cursor()

    print("===============Add a Author===========")
    fname = input("What is the authors first name: ")
    lname = input("What is the authors last name: ")
    while True:
        isbn = input("What is the ISBN for the book he wrote: ")

        cursor.execute("SELECT isbn FROM books WHERE isbn = %s", (isbn,))

        if cursor.fetchone() is None:
            print("Not vaild, choose again")
            continue
        else:
            break


    cursor.execute("INSERT INTO authors (fname, lname) VALUES (%s, %s) RETURNING uid", (fname, lname))
    temp = cursor.fetchone()
    uid = temp[0]

    cursor.execute("INSERT INTO author_has_book (author_uid, book_isbn) VALUES (%s, %s)", (uid, isbn))
    cursor.execute("SELECT uid FROM authors WHERE uid = %s", (uid,))

    if cursor.fetchone() is not None:
        print("author added")

    connection.commit()
    cursor.close()


def addBook(connection):
    cursor = connection.cursor()

    #get the book data
    print("Lets start adding a book!")
    isbn = input("What is the isbn of the book: ")
    name = input("What is the title of the book: ")
    pages = input("How many pages are in the book: ")
    price = input("What is the price of the book: ")
    quantity = input("How many of these books do you have in stock: ")
    percent = input("What is the publisher percentage: ")

    while True:
        email = input("What is the publisher's email: ")

        cursor.execute("SELECT email FROM publishers WHERE email = %s", (email,))
        if cursor.fetchone() is None:
            print("\nThat is not a vaild publisher email")
            continue
        else:
            break

    #add the book
    print("Adding book...")
    cursor.execute("INSERT INTO books(isbn, name, pages, price, quantity, publisher_share_percentage, publisher_email) VALUES (%s, %s, %s, %s, %s, %s, %s)", (isbn, name, pages, float(price), int(quantity), int(percent), email))

    #make sure it added
    cursor.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))
    if cursor.fetchone() is not None:
        print("Add successful")


    connection.commit()
    cursor.close()



def removeBook(connection):
    cursor = connection.cursor()

    while True:
        #get book isbn
        isbn = input("What is the ISBN for the book you want to delete? ")
        print("Okay, deleting now...")

        #make sure book exists
        cursor.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))

        if cursor.fetchone() is not None:
            #delete book
            cursor.execute("DELETE FROM books WHERE isbn = %s", (isbn,))
            print("Deletion complete")
            break
        
        #if book doesnt exist
        else:
            print("Sorry, a book with that ISBN does not exist")
            flag = False
            flag2 = False
            while True:
                userIn = input("Would you like to delete something else? (y/n)")
                if userIn == "y" or userIn == "Y":
                    flag = True
                elif userIn == "n" or userIn == "N":
                    flag2 = True
                    break
                else:
                    print("Sorry that was an invalid input, please type 'y' for yes or 'n' for no")
                break
            if flag:
                continue
            if flag2:
                break

    connection.commit()
    cursor.close()
