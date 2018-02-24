import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize

def smmm(text):
	x= summarize(text, ratio=0.1)
	print ('Summary:')
	print (x)
	
	print(len(text))
	print(len(x))
