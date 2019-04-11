orig=open('fr_sequoia-ud-test.conllu')
testout=open('fr_sequoia-ud-testout.conllu')
i=0
j=0
while i<353:
	origline=orig.readline()
	origline = origline.strip('\n')
	testoutline=testout.readline()
	testoutline = testoutline.strip('\n')
	if testoutline != origline:
		j+=1
		print("Difference", j)
		print("Original:", origline)
		print("testout:", testoutline)
	i+=1
orig.close()
testout.close()