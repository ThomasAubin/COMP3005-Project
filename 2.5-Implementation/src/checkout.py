import psycopg2

def checkout(uid, cart):
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

    while True:

        choice = input("What would you like to do 1. Checkout | 2. View Cart | 3. Return to main menu")

        if not choice.isdigit():
            print("\nsorry that is an invalid choice\n")
            continue
        elif int(choice) == 1:
            print()
            # ADD CHECK OUT FEATURE HERE
            for i in range(0, len(cart), 2):
                cursor.execute("SELECT * FROM Books WHERE ISBN = %s", (cart[i],))
                currentBook = cursor.fetchone()
                # print(currentBook)


                #create order
                #book has order

                cursor.execute("INSERT INTO OrderBooks(bookISBN, pricePerUnit, quantity, orderNum) VALUES (%s, %s, %s, %s)", (currentBook[0], currentBook[3], cart[i + 1], ))
                # cursor.execute("INSERT INTO OrderBooks(ISBN, name, pages, price, quantity, publisherSharePercentage, publisherEmail) VALUES (%s, %s, %s, %s, %s, %s, %s)", (isbn, name, pages, float(price), int(quantity), int(percent), email))")
                # print()

        elif int(choice) == 2:
            print("==============Cart===============\n")
            for i in range(0, len(cart), 2):
                print("ISBN: " + cart[i] + "         " + "Quantity: " + cart[i + 1])
            continue

        elif int(choice) == 3:
            break

        else:
            print("Sorry that was an invalid choice")
            continue








    #save data
    connection.commit()

    #close connections and cursor
    cursor.close()
    connection.close()

cart = ["1","2","2","2","3","2"]
checkout(0, cart)