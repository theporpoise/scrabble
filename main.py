

def a_lookup(user_tiles, board_tiles=""):
	tiles = []
	if(len(board_tiles) > 0):
		for i in board_tiles:
			tiles.append((user_tiles+i))
	for i in tiles:
		print "for the letter " + i[-1]

#a_lookup('cab', 'abc')

def b_lookup(user_tiles, board_tiles=None):
	tiles = []
	#print tiles
	if(board_tiles):
		print "you got here"
		#for i in board_tiles:
		#	tiles.append((user_tiles+i))
	for i in range(0, board_tiles):
		print "for the letter " + str(i)

b_lookup('cab', 5)