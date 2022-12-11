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

    flag = True
    total = 0

    while True:

        choice = input("What would you like to do 1. Checkout | 2. View Cart | 3. Return to main menu")

        if not choice.isdigit():
            print("\nsorry that is an invalid choice\n")
            continue
        elif int(choice) == 1:

            #create order
            print("\n==============Payment Details===============\n")
            cardNum = input("What is the payment card number: ")
            expiry = input("What is the card expiry date: ")
            digit3 = input("What is the security code: ")
            fname = input("What is your first name: ")
            lname = input("What is your last name: ")

            print("\n==============Billing Address=============")
            billNum = input("What is your street number: ")
            billStreet = input("What is your street name: ")
            billCity = input("What is your city: ")
            billPostalCode = input("What is your Postal Code: ")
            billCountry = input("What is the country: ")

            print("\n==============Shipping Address=============")
            shipNum = input("What is your street number: ")
            shipStreet = input("What is your street name: ")
            shipCity = input("What is your city: ")
            shipPostalCode = input("What is your Postal Code: ")
            shipCountry = input("What is the country: ")

            cursor.execute("INSERT INTO Order (payment_num, payment_expiry, payment_3_digit_code, payment_fname, payment_lname, payment_street_num, payment_street, payment_city, payment_postal_code, payment_country, ship_street_num, ship_street, ship_city, ship_postal_code, ship_country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING uid", (cardNum, expiry, digit3, fname, lname, billNum, billStreet, billCity, billPostalCode, billCountry, shipNum, shipStreet,shipCity,shipPostalCode, shipCountry))
            orderUid = cursor.fetchone()

            # print(orderUid) CHECK THIS PART IF FAILS

            while True:
                proceed = input("Would you like to complete this order (y,n) if not, you will have to re-enter shipping and payment information: ")
                if proceed == "y":
                    break
                elif proceed == "n":
                    flag = False
                    break
                else:
                    print("Sorry that was an invalid input")
                    continue
            
            if flag == False:
                continue

            for i in range(0, len(cart), 2):
                cursor.execute("SELECT * FROM Books WHERE ISBN = %s", (cart[i],))
                currentBook = cursor.fetchone()

                #calculate total
                total += (float(currentBook[3]) * cart[i + 1])

                # insert into the OrderBooks
                cursor.execute("INSERT INTO OrderBooks(book_ISBN, price_Per_Unit, quantity, order_Num) VALUES (%s, %s, %s, %s)", (currentBook[0], currentBook[3], cart[i + 1], orderUid))
                
                #decrease quantity
                cursor.execute("UPDATE books SET quantity = quantity - %s WHERE ISBN = %s", (cart[i + 1], currentBook[0]))
            
            #adds order to user_has_orders
            cursor.execute("INSERT INTO users_has_order(order_num, user_uid) VALUES (%s, %s)", (orderUid, uid))

            #update cart
            cart = []
            continue

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

# cart = ["1","2","2","2","3","2"]
# checkout(0, cart)