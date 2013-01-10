import sqlite3 as lite
import sys

con = lite.connect('words.db')

"""
with con:    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data                
"""    

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Words")
	cur.execute("CREATE TABLE Words(WHash, WArray)")
	cur.executemany("INSERT INTO Words VALUES(?, ?)", worder)
	
