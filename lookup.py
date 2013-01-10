"""MAKING A FASTER LOOKUP -  so these lookup functions are pretty slow.  The mysql select is even slower than the dictionary.  To make it faster, I could create a database of all 8 letter tile combinations and their corresponding words.  This way I don't have to run the function each time, I just do a lookup (run the function once and then stick it in the database.)  This would be much quicker...  The question then becomes will I be able to easily sort these answers, let's say, by length.  Or by what the first letter is, or 3rd letter, etc.  This is a good database challenge...  This returns over 200 billion letter combinations.  after quick look at the internet - this ain't feasible.  """

import itertools
from selecting import *
#Only if you are selecting from mysql database
from createdict import *
#only need to do this if you are using the dict instead of the database.  The dict is quicker b/c the set is small, but it is not applicable to larger datasets...

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

#finds a hash for a given letter combination
def convert(tiles):
	word_hash = 0
	for letter in tiles:
		if(letter == '-'):
			print tiles
			continue
		word_hash += lnum[letter]
	return str(word_hash)

#combos should generate the combination of letters to be turned to hashes
def combos(tiles):
	#takes a group of letters, returns list of all possible letter combinations of length 2 or greater....
	total_combos = []
	word_list = []
	for i in range(2, len(tiles) + 1):
		total_combos.extend([x for x in itertools.combinations(tiles, i)])
	
	word_list = []
	for group in total_combos:
		word = ""
		for i in range(0, len(group)):
			word += group[i]
		word_list.append(word)
	return word_list
	
def lookup(tiles):
	potentials = combos(tiles)
	p_hash = []
	for i in potentials:
		p_hash.append(convert(i))
	print len(p_hash)
	p_set = set(p_hash)
	print len(p_set)
	for i in p_set:
	#	print i
		if select_words(i):
			print select_words(i)

#must uncomment the import if you want to work	
def lookup_with_worder(tiles):
	potentials = combos(tiles)
	p_hash = []
	for i in potentials:
		p_hash.append(convert(i))
	#print len(p_hash)
	p_set = set(p_hash)
	#print len(p_set)
	num_p_set = []
	for i in p_set:
		num_p_set.append(int(i))
	easy_read_list = []
	for j in num_p_set:
		if j in worder:
			easy_read_list.extend(worder[j])
	easy_read_list.sort(key=len)
	#print easy_read_list
	return easy_read_list


def a_lookup(user_tiles, board_tiles=None, special_tile=None, position=None):
	tiles = []
	tiles.append(user_tiles)
	if board_tiles:
		for i in board_tiles:
			tiles.append((user_tiles+i))


	for i in tiles:
		if i == user_tiles:
			print "for just your tiles"
			print lookup_with_worder(i)
			continue
		print "for your tiles and the board letter " + i[-1]
		with_letter = lookup_with_worder(i)
		for j in with_letter:
			if i[-1] in j:
				print j
	
	#only executes if special tiles given
	if special_tile:
		if special_tile not in user_tiles:
			if special_tile not in board_tiles:
				print "You don't have that letter"
				return
		
		print "for words including the letter " + special_tile
		big_list = []
		for i in tiles:
			if special_tile in i:
				big_list.extend(lookup_with_worder(i))	
		#print big_list
		big_set = set(big_list)
		#print big_set
		
		big_list_w_letter = []
		for j in big_set:
			if special_tile in j:
				big_list_w_letter.append(j)
		small_set = set(big_list_w_letter)
		print small_set
		
		if (position > -2):
			print "for words including the letter " + special_tile + "at position " + str(position)
			for i in small_set:
				if i[int(position)] == special_tile:
					print i


#These are the two test functions that currently work.  lookup with worder is fast (but memory intensive).  Need to make lookup return nicer.  
#lookup("weaselo")
#lookup_with_worder("weaselo")

"""
test = convert('aseret')
print test

print select_words('10002000000000000111000000')
print select_words(test)
"""


"""
print combos('abcd')
lookup takes user input (their tiles) and returns a complete list of words they could use.  It uses combos to get combinations and sends each of those to convert.  It then creates a set of word_hashes (so as not to repeat itself.  It then sends the word hashes to query the database to pull out possible words.
"""

