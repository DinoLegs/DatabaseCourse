import mysql.connector

# returns a connection object
def connect():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='web-at-taket',
        database='courseDB'
    )
    return connection

# Create a new character
def create_character(profile_name, character_name, class_name):
    cnx = connect()

    # implement the function

    cnx.close()

def set_character_level():
    pass

def get_weapons_of_character():
    pass

def give_character_new_weapon():
    pass


if __name__ == "__main__":
    # Debug your code here!
    pass