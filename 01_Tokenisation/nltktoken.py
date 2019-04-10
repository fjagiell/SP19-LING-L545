import punkt
import nltk.tokenize.punkt
tokenizer=nltk.tokenize.punkt.PunktSentenceTokenizer()
import codecs
text=codecs.open('wiki.txt').read()
tokenizer.train(text)
import pickle
out=open('norman.pickle','wb')
pickle.dump(tokenizer,out)
out.close()