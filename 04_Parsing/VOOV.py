IN=open('UD_German-GSD/de_gsd-ud-train.conllu') #last run was German 
#file name replaced for each language
line='xx'
OV=0
VO=0
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
	if 'obj' in line[7]:
		object=line[0]
		object=int(object)
		verb=line[6]
		verb=int(verb)
		if object<verb:
			OV+=1
		if verb<object:
			VO+=1
VOprop=VO/(OV+VO)
OVprop=OV/(OV+VO)
print('verb-obj:',VOprop)
print('obj-verb:',OVprop)
print(OV)
print(VO)
IN.close()