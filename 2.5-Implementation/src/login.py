import psycopg2

def login():
    loginUsername = ""

    # set your database details here
    hostname = 'localhost'
    database = 'Look_Inna_Book'
    username = 'postgres'
    pwd = 'admin'
    portId = '5432'

    #initialise the connection and cursor
    connection = None
    cursor = None

    #try:
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
        print("================= LOGIN =================")
        username = input("Username: ")
        password = input("Password: ")

        cursor.execute("SELECT username FROM users WHERE username = %s AND password = %s", (username, password))
        loginUsername = cursor.fetchone()

        if loginUsername is None:
            print("sorry, there is an incorrect username or password")
            continue
        else:
            print("Login Successful")
            break


    #save the new things to the database
    connection.commit()

    #close connections and cursor
    cursor.close()
    connection.close()

    return loginUsername

