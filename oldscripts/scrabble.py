#import json
#import sqlite3 as lite
#import sys
#import string
#import itertools

lnum = dict(
	a = 10000000000000000000000000,
	b = 1000000000000000000000000,
	c = 100000000000000000000000,
	d = 10000000000000000000000,
	e = 1000000000000000000000,
	f = 100000000000000000000,
	g = 10000000000000000000,
	h = 1000000000000000000,
	i = 100000000000000000,
	j = 10000000000000000,
	k = 1000000000000000,
	l = 100000000000000,
	m = 10000000000000,
	n = 1000000000000,
	o = 100000000000,
	p = 10000000000,
	q = 1000000000,
	r = 100000000,
	s = 10000000,
	t = 1000000,
	u = 100000,
	v = 10000,
	w = 1000,
	x = 100,
	y = 10,
	z = 1
)

worder = {}

contents = open('web2').read().splitlines()

lcontents = [x.lower() for x in contents]

for word in lcontents:
	word_hash = 0
	for letter in word:
		if(letter == '-'):
			print word
			continue
		word_hash += lnum[letter]
	if(word_hash in worder):
		worder[word_hash].append(word)
	else:
		worder[word_hash] = [word]


a = string.ascii_lowercase



def convert(word):
	word_hash = 0
	word_combos = []
	for i in xrange(1, len(word)+1):
		els = [list(x) for x in itertools.combinations(word, i)]
		word_combos.extend(els)
	
	print word_combos
	
	for letter in word:
		if(letter == '-'):
			print word
			continue
		word_hash += lnum[letter]
	return word_hash


def addboard(user_letters, board = a):
	letters_array = []
	if len(board) == 0:
		letters_array.append(user_letters)
	hash_array = []
	possibles = []
	for b in board:
		letters_array.append(user_letters + b)
	for combos in letters_array:
		hash_array.append(convert(combos))
	for key in hash_array:
		if key in worder:
			possibles.append(worder[key])
	print possibles


		


	"""I'm currently at the point where I'm learning how to use itertools to create a list of possible combos that I can then send through my conversion function to return a list of word_hashes.  I will then need to take this and turn it into a list of words.  In here somewhere I need to check to see if there are duplicates, b/c as you remove letters you may get a duplicate.  I may be able to use a dictionary for that.  Also, when I wrote the search engine I made a cache that handled duplicates well.  I liked that set up.  Those are two thoughts.  

	When I got the logic to work the way I wanted, then I wanted to go back and explore creating a database with the words and then querying it to get the answer.

	After that, I was interested in creating a word object to hold the different possible answers and contain functions to interact with the user.

	NOW ON TO RUBY!"""

	"""specify the order like ???c??s????? - have to put as many question marks as there are blanks on either side -  and here are my letters 'abcdefg' """

"""
NOT SURE HOW TO CONNECT TO DATABASE YET, BUT FOR NOW WILL PLAY AROUND WITH THE CODE TO GENERATE ALL POSSIBLE WORD MATCHES AND SEE HOW THAT WORKS.

con = lite.connect('words.db')

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Words")
	cur.execute("CREATE TABLE Words(WHash, WArray)")
	cur.executemany("INSERT INTO Words VALUES(?, ?)", worder)
"""



"""
This created the neat JSON file, don't know why it would be useful...
f = open('words.json', 'w')
f.write(json.dumps(worder))
"""

"""
print contents[0]

00000000000000000000000000

def create():
	for word in contents:
		for letter in word:
			ord(letter) - 96
		
		contents[i] in worder:
			
		worder['contents[i]'] =contents
		if(contents[i] == "a"):
			print "this is it fool!"
		print contents[i]
		#print dictfile.readline()
		
#look(10)
"""


"""
new_contents = contents.replace('\n', '')
f = open('sansnl.txt', 'w')
f.write(new_contents)
f.close
"""

"""
worder = {}

arry = []

f = open("filename.ext", "w")

def look(num):
	global arry
	for i in range(0,num):
		a = dictfile.readline()
		arry += a
		#print dictfile.readline()
	

		
look(10)

print arry
"""		

"""Test Code:

making sure the number assignment dictionary works:

total = 0
for i in a:
	total += lnum[i]

print total, len(str(total))


a = string.ascii_lowercase



"""

"""
def get_hashes(word_array):
	hash_array = []
	for word in word_array:
		word_hash = convert(word)
		hash_array.append(word_hash)
	return hash_array
"""

#	if(worder[word_hash]):
#		return worder[word_hash]

#	else:
#		return "sorry, no words match!"