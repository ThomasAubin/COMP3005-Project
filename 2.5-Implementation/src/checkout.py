import psycopg2

def checkout(user_username, cart):
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

    flag = True
    total = 0

    while True:

        choice = input("What would you like to do 1. Checkout | 2. View Cart | 3. Return to main menu: ")

        if not choice.isdigit():
            print("\nSorry that is an invalid choice\n")
            continue
        elif int(choice) == 1:

            
            
            #useShip = input("Would you like to use the address on your account as shipping address (y/n): ")
            while True:
                useCard = input("Would you like to use use a card on your account (y/n): ")

                if useCard == "y" or useCard == "Y":
                    cursor.execute("SELECT num FROM paymentcards WHERE user_username = %s", (user_username,))
                    cards = cursor.fetchall()

                    if cards is None:
                        print("You do not have a card on file, select 'n'")
                        continue

                    print("Here are the card numbers: \n")
                    for card in cards:
                        print(card[i])
                    
                    cardNum = input("Please type the number of the card you want to use: ")

                    cursor.execute("SELECT num FROM paymentcards WHERE num = %s", (cardNum,))

                    if cursor.fetchone() is None:
                        print("That is not a vaild card number")
                        continue
                    
                    else:
                        cursor.execute("SELECT expiry FROM paymentcards WHERE num = %s", (cardNum,))
                        temp = cursor.fetchone()
                        expiry = temp[0]

                        cursor.execute("SELECT digit_code_3 FROM paymentcards WHERE num = %s", (cardNum,))
                        temp = cursor.fetchone()
                        digit3 = temp[0]

                        cursor.execute("SELECT fname FROM paymentcards WHERE num = %s", (cardNum,))
                        temp = cursor.fetchone()
                        fname = temp[0]

                        cursor.execute("SELECT lname FROM paymentcards WHERE num = %s", (cardNum,))
                        temp = cursor.fetchone()
                        lname = temp[0]
                    break
                    
                elif useCard == "n" or useCard == "N":
                    #create order
                    print("\n==============Payment Details===============\n")
                    cardNum = input("What is the payment card number: ")
                    expiry = input("What is the card expiry date: ")
                    digit3 = input("What is the security code: ")
                    fname = input("What is your first name: ")
                    lname = input("What is your last name: ")
                    break

                else:
                    print("That is not a valid option")
                    continue
            
            while True:
                useAddr = input("Would you like to use the address on our account as billing address (y/n): ")

                if useAddr == "y" or useAddr == "Y":
                    allAddr = []
                    cursor.execute("SELECT address_uid FROM user_has_address WHERE user_username = %s", (user_username,))
                    
                    addressUids = cursor.fetchall()

                    for address in addressUids:
                        cursor.execute("SELECT * FROM addresses WHERE uid = %s", address)
                        allAddr.append(cursor.fetchone())

                    print("Here are you saved addresses: \n")

                    for i in range(0, len(allAddr)):
                        print(i + ". " + allAddr[i][1] + " " + allAddr[i][2] + " " + allAddr[i][3] + " " + allAddr[i][4] + " " + allAddr[i][5])

                    useName = ""

                    while True:
                        useName = input("Please type the number of the address you want to use: ")

                        if not useName.isdigit():
                            print("That is not a vaild input")
                            continue
                        elif 0 > int(useName) or len(allAddr) <= int(useName):
                            print("That is not a vaild input")
                            continue
                        else:
                            break
                    
                    useName = allAddr[useName][0]
                        
                    cursor.execute("SELECT uid FROM addresses WHERE uid = %s", (useName,))

                    if cursor.fetchone() is None:
                        print("That is not a vaild uid")
                        continue

                    else:
                        cursor.execute("SELECT street_num FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        billNum = temp[0]

                        cursor.execute("SELECT street FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        billStreet = temp[0]

                        cursor.execute("SELECT city FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        billCity = temp[0]

                        cursor.execute("SELECT country FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        billCountry = temp[0]

                        cursor.execute("SELECT postal_code FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        billPostalCode = temp[0]
                    break   
                elif useAddr == "n" or useAddr == "N":
                    print("\n==============Billing Address=============")
                    billNum = input("What is your street number: ")
                    billStreet = input("What is your street name: ")
                    billCity = input("What is your city: ")
                    billPostalCode = input("What is your Postal Code: ")
                    billCountry = input("What is the country: ")
                    break
                else:
                    print("That is not a vaild option")
                    continue

            while True:
                useShip = input("Would you like to use the address on our account as shipping address (y/n): ")

                if useShip == "y" or useShip == "Y":
                    cursor.execute("SELECT address_uid FROM user_has_address WHERE user_username = %s", (user_username,))
                    
                    addressUids = cursor.fetchall()

                    print("Here are you saved addresses: \n")
                    for uid in addressUids:
                        cursor.execute("SELECT uid, name FROM addresses WHERE uid = %s", (uid,))
                        name = cursor.fetchall()
                        print("UID: " + uid + "         " + "Name: " + name)

                    useName = input("Please type the UID of the address you want to use: ")

                    cursor.execute("SELECT uid FROM addresses WHERE uid = %s", (useName,))

                    if cursor.fetchone() is None:
                        print("That is not a vaild uid")
                        continue

                    else:
                        cursor.execute("SELECT street_num FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        shipNum = temp[0]

                        cursor.execute("SELECT street FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        shipStreet = temp[0]

                        cursor.execute("SELECT city FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        shipCity = temp[0]

                        cursor.execute("SELECT country FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        shipCountry = temp[0]

                        cursor.execute("SELECT postal_code FROM addresses WHERE uid = %s", (useName,))
                        temp = cursor.fetchone()
                        shipPostalCode = temp[0]
                    break   

                elif useShip == "n" or useShip == "N":
                    print("\n==============Shipping Address=============")
                    shipNum = input("What is your street number: ")
                    shipStreet = input("What is your street name: ")
                    shipCity = input("What is your city: ")
                    shipPostalCode = input("What is your Postal Code: ")
                    shipCountry = input("What is the countrys: ")
                    print("before break")
                    break

                else:
                    print("That is not a vaild option")
                    continue

            print("before order")

            cursor.execute("INSERT INTO orders(bill_num, bill_expiry, bill_digit_code_3, bill_fname, bill_lname, bill_street_num, bill_street, bill_city, bill_postal_code, bill_country, ship_street_num, ship_street, ship_city, ship_postal_code, ship_country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING num", (cardNum, expiry, digit3, fname, lname, billNum, billStreet, billCity, billPostalCode, billCountry, shipNum, shipStreet,shipCity,shipPostalCode, shipCountry))
            orderUid = cursor.fetchone()

            

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
            

            #cursor.execute("INSERT")
            for i in range(0, len(cart), 2):
                print("in loop")
                cursor.execute("SELECT * FROM books WHERE isbn = %s", (cart[i],))
                currentBook = cursor.fetchone()

                #calculate total
                total += (float(currentBook[3]) * float(cart[i + 1]))

                # insert into the OrderBooks
                cursor.execute("INSERT INTO order_has_book(book_isbn, price_per_unit, quantity, order_num) VALUES (%s, %s, %s, %s)", (currentBook[0], currentBook[3], cart[i + 1], orderUid))
                
                #decrease quantity
                cursor.execute("UPDATE books SET quantity = quantity - %s WHERE isbn = %s", (int(cart[i + 1]), currentBook[0]))

            print("Your Order number is: " + str(orderUid))
            print("Your Order total was: " + str(total))
            print("Checkout successful")

            
            # #adds order to user_has_orders##########
            # cursor.execute("INSERT INTO users_has_order(order_num, user_uid) VA1
            # LUES (%s, %s)", (orderUid, uid))

            #update cart
            cart = []
            print("==============Cart===============\n")
            for i in range(0, len(cart), 2):
                print("ISBN: " + cart[i] + "         " + "Quantity: " + cart[i + 1])
            break


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