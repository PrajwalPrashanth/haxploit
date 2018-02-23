## remove stop words

'''from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

ex = "we can easily encode the first fact using standard inheritance any frame with bird on it inheritance slot inherits the value 2 on its legs slot"

stop_words = set(stopwords.words("english"))

words = word_tokenize(ex)

filtered_sentence = []

for w in words:
	if w not in stop_words:
		filtered_sentence.append(w)

print (filtered_sentence)'''


## output:['easily', 'encode', 'first', 'fact', 'using', 'standard', 'inheritance', 'frame', 'bird', 'inheritance', 'slot', 'inherits', 'value', '2', 'legs', 'slot']