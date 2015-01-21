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
			print(word)
			continue
		word_hash += lnum[letter]
	if(word_hash in worder):
		worder[word_hash].append(word)
	else:
		worder[word_hash] = [word]
