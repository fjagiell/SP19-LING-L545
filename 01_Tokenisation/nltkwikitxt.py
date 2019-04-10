line='a'
i=0
IN=open('wiki.txt')
while line and i<50:
	line=IN.readline()
	i+=1
	from nltk.tokenize import sent_tokenize
	sent_tokenize_list = sent_tokenize(line)
	for j in range(0,len(sent_tokenize_list)):	
		print(sent_tokenize_list[j])
IN.close()