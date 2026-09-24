# This is a basic example of how you can use the mysql connector. 

import mysql.connector

cnx = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='web-at-taket',
    database='courseDB'
)

cursor = cnx.cursor()

cursor.execute('SELECT * FROM profile')

for (username, password) in cursor:
    print(f"username: {username}, password: {password}")
# to get data from a query you can also run 
# row = cursor.fetchone() # returns a tuple
# rows = cursor.fetchall() # returns a list of tuples

cursor.execute("INSERT INTO profile VALUES ('name', 'pass')") # this will fail if run twice without changing values

cnx.commit() # this is neccesary to perform the insert