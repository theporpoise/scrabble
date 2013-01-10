"""b/c what I needed to do was very simple, I ended up going to the console, opening mysql, creating the database and table, and manually entering it in.  I learned that mysql is very particular about how you load text files and that i needed to use FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n' b/c I think that this is what textmate uses - stupid textmate!  lol.  to specify it correctly.  This seemed to solve the problem."""


import MySQLdb

wordlistpath = "/Users/matthewgould/Documents/pythonscripts/scrabble/wordlist.csv"

connection = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
		db = 'wldb'
)

cursor = connection.cursor()

query = "LOAD DATA INFILE '/Users/matthewgould/Documents/pythonscripts/scrabble/wordlist.csv' INTO TABLE words FIELDS TERMINATED BY ',' LINES TERMINATED BY '\r\n'"

cursor.execute(query)
connection.commit()

print "Done"

#import csv

"""To to this I ended up going to the console and typing mysql to launch mysql.  I then created the database and the table from there.  I couldn't figure out how to create the database from this file... lol.  I actually created the database by accident.  I think probably I just connect using a connection and specifying just a user.  Then create the databases and the tables.  Then close connection.  And open a new connection to the database I created.  But it's easy to just launch mysql and create one.  Manipulating it from pyton is probably better though..."""