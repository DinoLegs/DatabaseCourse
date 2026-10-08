import mysql.connector

# returns a connection object
def connect():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='<password>',
        database='<database>'
    )
    return connection

# Create a new character
def create_profile(profile_name, password):
    cnx = connect()
    cursor = cnx.cursor()

    cursor.execute(f'''INSERT INTO user VALUES 
        ('{profile_name}', '{password}')''')

    cnx.commit()
    cnx.close()

# Change level of a character
def set_character_level(profile_name, character_name, level):
    cnx = connect()
    cursor = cnx.cursor()

    cursor.execute(f'''UPDATE characters 
        SET characterLevel = '{level}'
        WHERE username = '{profile_name}' 
        AND characterName = '{character_name}' ''')

    cnx.commit()    
    cnx.close()

# Return a list of all characters a profile has
def get_characters_of_player(profile_name):
    cnx = connect()
    cursor = cnx.cursor()

    cursor.execute(f'''SELECT characterName FROM user
        INNER JOIN characters
        ON characters.username = user.username
        WHERE user.username = '{profile_name}'
        ''', map_results=True)

    
    names = cursor.fetchall()
    print(names)
    while cursor.nextset():
        names = cursor.fetchall()
        print(names)
    cnx.close()

# Retrun a list of all weapons a character has
def get_weapons_of_character(profile_name, character_name):
    pass

# Give a character a new weapon
def give_character_new_weapon(profile_name, character_name, weapon):
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
    get_characters_of_player("a'; SELECT * FROM user WHERE ''='")
