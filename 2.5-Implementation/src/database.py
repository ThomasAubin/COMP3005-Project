import psycopg2

def connect():
    hostname = 'localhost'
    database = 'look_inna_book'
    username = 'postgres'
    pwd = 'admin'
    portId = '5432'

    try:
        connection = psycopg2.connect(host = hostname,
                                      dbname = database,
                                      user = username,
                                      password = pwd,
                                      port = portId)

        print("Database connected successfully")
    except Exception as error:
        print(error)
        print("Database not connected successfully. Terminating program\n")
        exit()

    return connection
