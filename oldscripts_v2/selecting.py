import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="wldb")

c = db.cursor()

def select_words(word_hash):
	#narrow down the query to the words I want
	c.execute("SELECT word FROM wordlist2 WHERE word_hash=%s", (word_hash))
	#put this array of words into a variable
	data_array = c.fetchall()
	#print data_array
	return data_array
		


#select_words('11100000000000000000000000')

#c.execute("SELECT word_hash, word FROM words WHERE word_hash='10000000000000000000000000'")
#print c.fetchall()
