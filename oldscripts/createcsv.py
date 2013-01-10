import csv
from createdict import *



f = open('wordlist.csv', 'wt')

try:
	writer = csv.writer(f)
	writer.writerow( ('word_hash', 'word'))
	for key in worder:
		for word in worder[key]:
			writer.writerow( ( key, word))
finally:
	f.close()
	
print open('wordlist.csv', 'rt').read()









