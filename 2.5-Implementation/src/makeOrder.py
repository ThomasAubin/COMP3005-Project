import psycopg2



#returns an array with the isbn and quantity
def makeOrder():
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

    order = []
    while True:
        # get books and quantity
        choice = input("\nWhat would you like to do 1. Get more books | 2. view cart | 3. Return back to the main page: ")

        if not choice.isdigit():
            print("\nsorry that is an invalid choice\n")
            continue

        elif int(choice) == 1:
            while True:
                tempBook = input("What is the ISBN of the book you want to order: ")
                tempQuant = input("How many of these would you like to buy: ")

                #check if book exists
                cursor.execute("SELECT * FROM Books WHERE ISBN = %s", (tempBook,))

                #if book doesnt exist
                if cursor.fetchone() is None:
                    print("Sorry that book does not exist, please enter a vaild ISBN")
                    continue
                #if it does, add the book to cart
                else:
                    duplicate = False

                    #if item already in cart, increment quantity
                    for i in range(0, len(order), 2):
                        if order[i] == tempBook:
                            temp = order[i + 1]
                            total = int(temp) + int(tempQuant)

                            order[i + 1] = str(total)
                            duplicate = True
                            break
                    # add item if not existing
                    if not duplicate:
                        order.append(tempBook)
                        order.append(tempQuant)
                    break
            continue

        # display cart
        elif int(choice) == 2:
            print("==============Cart===============\n")
            for i in range(0, len(order), 2):
                print("ISBN: " + order[i] + "         " + "Quantity: " + order[i + 1])
            continue

        #return to main menu
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

    return order

#makeOrder()




