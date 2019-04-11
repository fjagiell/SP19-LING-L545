# thereisacat.

# firstword = 'thereisacat.'
# remainder = ''

# firstword = 'thereisacat'
# remainder = '.'

import sys

def maxmatch(sentence, dictionary):
	if sentence=='':
		return([])
	for i in range(len(sentence),0,-1):
		firstword=sentence[:i+1]
		remainder=sentence[i+1:]
		if firstword in dictionary:
			return([firstword, remainder])
	firstword=sentence[0]
	remainder=sentence[1:]
	return([firstword, remainder ])
dictionary=open('jadict.txt').read().split('\n')
for sentence in sys.stdin.readlines():

#sentence=input()
	while sentence:
		w=maxmatch(sentence, dictionary)
		print(w[0]+' ',end='')
		sentence=w[1]
	#print()