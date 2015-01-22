import itertools

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

# Creating the dictionary hash.  Takes the dictionary, formats it to lowercase, creates a word hash for each word.
# This word hash is a cool trick to look up if you can make that word from your tiles by converting it
# to a number, creates a faster lookup.  It is a list of potential words that contain those tiles.
# so instead of returning alphabetical words, etc, it has this list of words for that given letter value.


worder = {}
#This is the global dictionary that contains all possible words in web2 dictionary sorted by their letter value.

contents = open('web2').read().splitlines()
#Opening file and putting it ito a list

lcontents = [x.lower() for x in contents]
#formatting the list to lowercase

for word in lcontents:
	word_hash = 0
	for letter in word:
		if(letter == '-'):
			print(word)
			continue
		word_hash += lnum[letter]
	if(word_hash in worder):
		worder[word_hash].append(word)
	else:
		worder[word_hash] = [word]

#goes through every word in the dictionary and appends it to the appropriate hash value.
# for instance, this is the letters 'atb' print(worder[11000000000000000001000000])
# and this is 'atb' converted print(convert('bat'))


####
#finds a hash for a given letter combination
def convert(tiles):
	word_hash = 0
	for letter in tiles:
		if(letter == '-'):
			print(tiles)
			continue
		word_hash += lnum[letter]
	return str(word_hash)


#combos should generate the combination of letters to be turned to hashes
def combos(tiles):
	#takes a group of letters, returns list of all possible letter combinations of length 2 or greater, removes duplicates.
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
	return easy_read_list


my_tiles = "idulmdmo"

print(convert(my_tiles))
print(combos(my_tiles))
print(lookup_with_worder(my_tiles))


# To do:
'''
this is a comment

convert words to point values, show highest point values first (easy).

Find all possible places to play, then find highest value play at that location.
--> locations function, finds all possible locations to play
		*to be a possible location, must be a valid spot to play, and you have tiles to play.
		*How you define location is interesting.  Location is most likely defined as set of unique set of tiles.
			*This means there are a whole shit ton of locatoins!
--> highest value at location function

Find what are locations?
--> what_locations function
--> this is defined by current tiles, except in the instance of starting play.
--> For starting play, finding highest value should be easy.

Simplifying Assumptions (cross these off one by one)
	There are no board tiles (done)
	There are no points
	There is no board state / playable area

 


BLANK	2	0
A	9	1
B	2	4
C	2	4
D	5	2
E	13	1
F	2	4
G	3	3
H	4	3
I	8	1
J	1	10
K	1	5
L	4	2
M	2	4
N	5	2
O	8	1
P	2	4
Q	1	10
R	6	1
S	5	1
T	7	1
U	4	2
V	2	5
W	2	4
X	1	8
Y	2	3
Z	1	10

create a board state (hard)
-> current board state
-> available play area
-> dealing with board letters
-> adding in value to the board state





'''


