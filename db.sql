DROP DATABASE IF EXISTS courseDB;
CREATE DATABASE courseDB;
USE courseDB

CREATE TABLE user(
    username VARCHAR(50) PRIMARY KEY,
    pass VARCHAR(50) NOT NULL
);

INSERT INTO user VALUES 
    ('A.Turing', 'IDoneSolvedEnigma'),
    ('GHopps', 'TheOGCompiler');

CREATE TABLE class(
    className ENUM('barbarian', 'wizard', 'rogue') PRIMARY KEY,
    strBase FLOAT NOT NULL,
    dexBase FLOAT NOT NULL,
    conBase FLOAT NOT NULL,
    intBase FLOAT NOT NULL, 
    strMod FLOAT NOT NULL,
    dexMod FLOAT NOT NULL,
    conMod FLOAT NOT NULL,
    intMod FLOAT NOT NULL
);

INSERT INTO class VALUES
    ('barbarian', 1E1, 7E0, 1.2E1, 2E0, 2E0, 1.5E0, 1E0, 5E-1),
    ('wizard', 1E0, 5E0, 3E0, 2E1, 1.2E0, 1E0, 7.5E-1, 2E0),
    ('rogue', 5E0, 1.5E1, 7E0, 8E0, 2E0, 1.5E0, 1E0, 5E-1);

CREATE TABLE characters( 
	username VARCHAR(50), 
	characterName VARCHAR(50), 
	className ENUM('barbarian', 'wizard', 'rogue') NOT NULL, 
	characterLevel INT(8) DEFAULT 0, 
	FOREIGN KEY (username) REFERENCES user(username),
    FOREIGN KEY (className) REFERENCES class(className),
	PRIMARY KEY (username, charactername)
);

INSERT INTO characters(username, characterName, className) VALUES
    ('A.Turing', 'Balthor the Destroyer', 'barbarian'),
    ('A.Turing', 'Sneaky Snek', 'rogue'),
    ('GHopps', 'Gandalf the Wise', 'wizard');

CREATE TABLE weapons(
	weaponName VARCHAR(50) PRIMARY KEY,
	damage INT NOT NULL,
    reqStr FLOAT NULL,
    reqDex FLOAT NULL,
    reqCon FLOAT NULL,
    reqInt FLOAT NULL
);

INSERT INTO weapons(weaponName, damage) VALUES 
    ('Basic Sword', 3);
INSERT INTO weapons(weaponName, damage, reqStr) VALUES
    ('Hammer of Destruction', 20, 1E1);
INSERT INTO weapons(weaponName, damage, reqInt) VALUES
    ('Wand of Superior Intelligence', 25, 1.7E1);

CREATE TABLE characterHasWeapon(
	username VARCHAR(50),
    characterName VARCHAR(50),
    weaponName VARCHAR(50),
    FOREIGN KEY (username, characterName) 
        REFERENCES characters(username, characterName) 
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (weaponName) 
        REFERENCES weapons(weaponName) 
        ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (username, charactername, weaponName)
);
