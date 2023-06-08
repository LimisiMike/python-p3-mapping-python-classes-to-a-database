import sqlite3

CONN = sqlite3.connect('music.db') #is equal to a hash that contains our connection to the database
CURSOR = CONN.cursor() #Allows us to interact with the database