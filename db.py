import mysql.connector

# returns a connection object
def connect():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password="<root_password>",
        database='courseDB'
    )
    return connection

# Create a new character
def create_character(profile_name, character_name, class_name):
    cnx = connect()

    # implement the function

    cnx.close()

# Change level of a character
def set_character_level(profile_name, character_name, level):
    pass

# Retrun a list of all weapons a character has
def get_weapons_of_character(profile_name, character_name):
    pass

# Give a character a new weapon
def give_character_new_weapon(profile_name, character_name, weapon):
    pass

# Return a list of all characters a profile has
def get_characters_of_player(profile_name):
    pass

# Return a list of the stats of a specified character
def get_character_stat(profile_name, charcter_name, stat):
    pass

# Return a list of strings of all the available names of the stats. 
def get_all_available_stats():
    pass

# return a list of the base stats of the specified class.
def get_base_stats_of_class(class_name):
    pass

# Return a list of all the available weapons
def get_all_available_weapons():
    pass

if __name__ == "__main__":
    # Debug your code here!
    pass