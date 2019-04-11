IN=open('ja_gsd-ud-test.conllu')
line='xx'
dico=[]
while True:
	line=IN.readline()
	if not line: 
		break
	line = line.strip('\n')
	if line == '':
		continue
	if line[0]=='#':
		continue
	line=line.split()
	dico.append(line[1])	
dicset=set(dico)
newdic=list(dicset)
print(len(dico))
print(len(dicset))
print(len(newdic))
words=''
for i in range(0,len(newdic)):
	words+=newdic[i]

OUT=open('jadicttest.txt','w')
OUT.write(words)
#for i in range(0,len(newdic)):
#	OUT.write(newdic[i]+'\n')
IN.close()
print(len(dico))
print(len(newdic))
OUT.close()
