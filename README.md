# Orbit database and mysql course

This repo is for the orbit database and mysql. 
For documentation for how to use the mysql python connector look [here](https://dev.mysql.com/doc/connector-python/en/)
For documentation on general use of mysql look [here](https://www.w3schools.com/mysql/default.asp)

## Setup
**NOTE:** This course assumes you have python and MySQL installed. 
First create a python virtual environment

`python -m venv .venv`

then activate that environment

Bash:

`source .venv/bin/activate`

Windows cmd:

`.venv/Scripts/activate.bat`

Windows powershell:

`.venv/Scripts/Activate.ps1`

Then install the required packages:

`python -m pip install -r requirements.txt`

## Tasks
### Step 1
JRPGOnline is a new game that is being developed by SickGamesCorp. The game is a fantasy 
multiplayer role playing game. We are tasked with writing the database for the game. 

The game has login with unique username and password. Every profile can create and play as 
arbitrarily many characters. The characters have a name, class, level and stats (strength, 
dexterity, constitution, intelligence). Every character starts at level 0. Each class comes 
with base stats and you get a boost to your stats for each level given by the formula:

`stat = baseStat + modifier * level`

the base stats and modifier are given by the below tables:

Barbarian:
|Stat |Base  |Modifier |
|Str  |10    |2        |
|Dex  |7     |1.5      |
|Con  |12    |1        |
|Int  |2     |0.5      |

Wizard:
|Stat |Base  |Modifier |
|Str  |1     |1.2      |
|Dex  |5     |1        |
|Con  |3     |0.75     |
|Int  |20    |2        |

Rouge:
|Stat |Base  |Modifier |
|Str  |5     |2        |
|Dex  |15    |1.5      |
|Con  |7     |1        |
|Int  |8     |0.5      |

Every character can also have weapons, for example "Basic Sword", "Hammer of Destruction" and 
"Wand of Superior Intelligence". For "Hammer of Destruction" you need a strength larger or equal 
to 10 to use. And for the "Wand of Superior Intelligence" you need an intelligence greater or 
equal to 17. 

Create a database that follows the task description and add in data for the three weapons, the 
three classes, a profile, and two characters for that profile. 

### Step 2
Connect to the database in `db.py`. This file has some functions to access the data in the 
database implement these functions. 

### Step 3
Our database is suseptible to SQL injection. This could be fixed by using prepared statements, 
but we are not going to do this. Instead we are going to create a user that doesn't have access
to sensitive data and use that to preform our SQL statements.

(For the tech stack that lifesupport uses, SQL injections are prevented by using prisma syntax 
for accessing the database. Even so we should still limit the access of our users so that they
can't be exploited.) 

### Step 4
SickGamesCorp. have decided to add a PvP element to JRPGOnline, but they don't want to ruin the 
game for those that don't want to participate. To do this they want every character to have a 
boolean field that specifies if the character can do PvP. Additionally they want to have a table
that keeps track of the score between players (How many times they have beaten each other).

Create these changes and a function to return a leaderboard of the 10 players with the highest 
PvP scores and the number of kills they have. Try to do this with just SQL and not any python
data processing. 
