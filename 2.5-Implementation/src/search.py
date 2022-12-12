import psycopg2


def displayBook(books):

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

    authorNames = []
    finalNames = ""
    finalGenre = ""

    # loop through for every book
    for book in books:
        #Get author names------------------------------------
        # get all author uids based on ISBN
        if len(books) == 7:
            book = books
        cursor.execute("SELECT author_uid FROM author_has_book WHERE book_isbn = %s", (book[0],))
        authorUIDs = cursor.fetchall()

        # get all the names of the authors for that book
        for author in authorUIDs:
            cursor.execute("SELECT fname, lname FROM authors WHERE uid = %s", (author,))
            authorName = cursor.fetchall()
            authorNames.append(str(authorName[0][0]) + " " + str(authorName[0][1]))

        #turn authors into string
        for name in authorNames:
            finalNames += name + ", "

        #Get genres------------------------------------------
        # get all genres based on ISBN
        cursor.execute("SELECT genre FROM genres WHERE book_isbn = %s", (str(book[0]),))
        genreNames = cursor.fetchall()

        # get all turn genres into string
        for genre in genreNames:
            finalGenre += genre + ", "


        #Get Publisher----------------------------------------
        if len(books) == 7:
            book = books

        cursor.execute("SELECT name FROM publishers WHERE email = %s", (str(book[6]),))
        publisherName = cursor.fetchall()
        finalPublish = publisherName


        # print book data--------------------------------------
        print("Title: " + str(book[1]))
        print("ISBN: " + str(book[0]))
        print("Number of pages: " + str(book[2]))
        print("Price: " + str(book[3]))
        print("Authors: " + str(finalNames))
        print("Genres: " + str(finalGenre))
        print("Publisher: " + str(finalPublish))
    
    #save data
    connection.commit()


    #close connections and cursor
    cursor.close()
    connection.close()


#----------------------------------------------------------------------------------------------------------------------

def search():
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

    while True:
        #ask for search input
        userIn = input('''\nWhat are you searching by?
        1. Book name
        2. Author
        3. ISBN
        4. Genre
        5. Quit\n''')

        if not userIn.isdigit():
            print("Sorry that was an invalid input, please select an option (1, 2, 3, 4, 5)")
            continue

        #search by book name----------------------------------
        if int(userIn) == 1:
            bookName = input("What is the book name: ")
            cursor.execute("SELECT * FROM books WHERE name = %s", (bookName,))

            rows = cursor.fetchall()

            if len(rows) == 0:
                print("Sorrys, there are no books that match that description")
                continue

            displayBook(rows)
            continue

        #search by author name---------------------------------
        elif int(userIn) == 2:
            books = []
            #get the aurthors name and find his UID
            authorName = input("What is the author's name (first name and last name): ")
            temp = authorName.split()
            firstName = temp[0]
            lastName = temp[1]
            cursor.execute("SELECT uid FROM authors WHERE fname = %s AND lname = %s", (firstName, lastName))
            temp = cursor.fetchone()
            authorUID = temp[0]

            # find the all ISBN the beling to authorUID
            cursor.execute("SELECT book_isbn FROM author_has_book WHERE author_uid = %s", (str(authorUID),))
            bookISBNs = cursor.fetchall()

            # retreive all books with the ISBN
            for isbn in bookISBNs:
                cursor.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))
                books.append(cursor.fetchone())
            
            if len(books) == 0:
                print("Sorry, there are no books that match that description")
                continue
            
            #print out books
            displayBook(books)
            continue
        
        #search by ISBN-----------------------------------------
        elif int(userIn) == 3:
            isbn = input("What is the book ISBN: ")
            cursor.execute("SELECT * FROM Books WHERE isbn = %s", (str(isbn),))

            rows = cursor.fetchone()
            print(rows)

            if len(rows) == 0:
                print("Sorry, there are no books that match that description")
                continue

            displayBook(rows)
            continue
        
        #search by genre---------------------------------------
        elif int(userIn) == 4:
            allBooks = []
            userGenre = input("What genre are you intrested in: ")
            cursor.execute("SELECT book_isbn FROM genres WHERE genre = %s", (userGenre,))
            genreISBN = cursor.fetchall()

            for isbn in genreISBN:
                cursor.execute("SELECT * FROM Books WHERE isbn = %s", (isbn,))
                allBooks.append(cursor.fetchone())
            
            if len(allBooks) == 0:
                print("Sorry, there are no books that match that genre")
                continue
            
            displayBook(allBooks)
            continue

        # quit option-------------------------------------------
        elif int(userIn) == 5:
            break

        else:
            print("Sorry that was an invalid input, please select an option (1, 2, 3, 4, 5)")
            continue
    
    #save data
    connection.commit()


    #close connections and cursor
    cursor.close()
    connection.close()



#search()






