import psycopg2


def displayBook(books):

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

    authorNames = []
    finalNames = ""
    finalGenre = ""

    # loop through for every book
    for book in books:
        #Get author names------------------------------------
        # get all author uids based on ISBN
        cursor.execute("SELECT Author_UID FROM book_has_authors WHERE Book_ISBN = %s", (book[0],))
        authorUIDs = cursor.fetchall()

        # get all the names of the authors for that book
        for author in authorUIDs:
            cursor.execute("SELECT fname, lname FROM Authors WHERE UID = %s", (author,))
            authorNames.append(author[0] + " " + author[1])

        #turn authors into string
        for name in authorNames:
            finalNames += name + ", "

        #Get genres------------------------------------------
        # get all genres based on ISBN
        cursor.execute("SELECT Genre FROM Genres WHERE Book_ISBN = %s", (book[0],))
        genreNames = cursor.fetchall()

        # get all turn genres into string
        for genre in genreNames:
            finalGenre += genre + ", "

        #Get Publisher----------------------------------------
        cursor.execute("SELECT fname, lname FROM Publishers WHERE email = %s", (book[6],))
        publisherName = cursor.fetchall()
        finalPublish = publisherName[0] + " " + publisherName[1]


        # print book data--------------------------------------
        print("Title: %s", book[1])
        print("ISBN: %s", book[0])
        print("Number of pages: %s", book[2])
        print("Price: %s", book[3])
        print("Authors: %s", finalNames)
        print("Genres: %s", finalGenre)
        print("Publisher: %s", finalPublish)
    
    #save data
    connection.commit()


    #close connections and cursor
    cursor.close()
    connection.close()


#----------------------------------------------------------------------------------------------------------------------

def search():
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
        #ask for search input
        userIn = input('''\nWhat are you searching by?
        1. Book name
        2. Author
        3. ISBN
        4. Genre
        5. Quit''')

        #search by book name----------------------------------
        if userIn == 1:
            bookName = input("What is the book name: ")
            cursor.execute("SELECT * FROM Books WHERE name = %s", (bookName,))

            rows = cursor.fetchall()

            if len(rows) == 0:
                print("Sorry, there are no books that match that description")
                continue

            displayBook(rows)
            continue

        #search by author name---------------------------------
        elif userIn == 2:
            books = []
            #get the aurthors name and find his UID
            authorName = input("What is the author's name (first name and last name): ")
            temp = authorName.split()
            firstName = temp[0]
            lastName = temp[1]
            cursor.execute("SELECT UID FROM Authors WHERE fname = %s AND lname = %s", (firstName, lastName))
            authorUID = cursor.fetchall()

            # find the all ISBN the beling to authorUID
            cursor.execute("SELECT Book_ISBN FROM book_has_authors WHERE Author_UID = %s", (authorUID,))
            bookISBNs = cursor.fetchall()

            # retreive all books with the ISBN
            for isbn in bookISBNs:
                cursor.execute("SELECT * FROM Books WHERE ISBN = %s", (isbn,))
                books.append(cursor.fetchone())
            
            if len(books) == 0:
                print("Sorry, there are no books that match that description")
                continue
            
            #print out books
            displayBook(books)
            continue
        
        #search by ISBN-----------------------------------------
        elif userIn == 3:
            isbn = input("What is the book ISBN: ")
            cursor.execute("SELECT * FROM Books WHERE ISBN = %s", (isbn,))

            rows = cursor.fetchone()
            if len(rows) == 0:
                print("Sorry, there are no books that match that description")
                continue

            displayBook(rows)
            continue
        
        #search by genre---------------------------------------
        elif userIn == 4:
            allBooks = []
            userGenre = input("What genre are you intrested in: ")
            cursor.execute("SELECT Book_ISBN FROM Genres WHERE Genre = %s", (userGenre,))
            genreISBN = cursor.fetchall()

            for isbn in genreISBN:
                cursor.execute("SELECT * FROM Books WHERE ISBN = %s", (isbn,))
                allBooks.append(cursor.fetchall())
            
            if len(allBooks) == 0:
                print("Sorry, there are no books that match that genre")
                continue
            
            displayBook(allBooks)
            continue

        # quit option-------------------------------------------
        elif userIn == 5:
            break

        else:
            print("Sorry that was an invalid input, please select an option (1, 2, 3, 4, 5)")
            continue
    
    #save data
    connection.commit()


    #close connections and cursor
    cursor.close()
    connection.close()










