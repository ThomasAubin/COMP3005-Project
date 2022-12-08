import psycopg2

hostname = 'localhost'
database = 'Look_Inna_Book'
username = 'postgres'
pwd = 'admin'
portId = '5432'

connection = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = portId)


connection.close()