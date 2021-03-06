from nltk.corpus import gutenberg
from nltk.probability import FreqDist

### what corpora are in the collection?
print gutenberg.fileids()

### create frequency dist object
fd = FreqDist()
### for each token in the relevant text increment its counter
for word in gutenberg.words('austen-persuasion.txt'):
	fd.inc(word)

### total number of samples
print fd.N()

### number of unique samples
print fd.B()

### get a list of the top 10 words sorted by freq
for word in fd.keys()[:10]:
	print word, fd[word]


### Exploring the corpora

import matplotlib

import matplotlib.pyplot as plt

### matplotlib.use('TkAgg')

### Count each token in each text of the Gutenberg collection:
fd = FreqDist()
for text in gutenberg.fileids():
	for word in gutenberg.words(text):
		fd.inc(word)


### initialize two empty lists which will hold out ranks and frequencies

ranks = []
freqs = []

### Generate a (rank, frequency) point for each counted token

for rank, word in enumerate(fd):
	ranks.append(rank+1)
	freqs.append(fd[word])


### Plot rank vs frequency on a log-log plot

plt.loglog(ranks, freqs)
plt.xlabel('frequency(f)', fontsize=14, fontweight='bold')
plt.ylabel('rank(r)', fontsize=14, fontweight='bold')
plt.show()

print 'got here'


### PREDICTING WORDS
from nltk.probability import ConditionalFreqDist
from random import choice

### Create a distribution object
cfd = ConditionalFreqDist()

### For each token count current word given previous word
prev_word = None
for word in gutenberg.words('austen-persuasion.txt'):
	cfd[prev_word].inc(word)
	prev_word = word


print cfd

### Start predicting at the gived word
word = 'therefore'
i = 1
keepSent = ""
### Find all words that can possibly follow the current word
### choose one at random

while i < 20:
	keepSent += " " + word
###	print str(i) + " " + word
	lwords = cfd[word].samples()
###	print lwords
	follower = choice(lwords)
###	print follower
	word = follower
	i += 1


print "-" * 50
### print keepSent



### DISCOVERING PART OF SPEECH TAGS
### ANALYZING TAGGED CORPORA
from nltk.corpus import brown
from nltk import FreqDist, ConditionalFreqDist

fd = FreqDist()
cfd = ConditionalFreqDist()


### get the (token,tag) pair for each tagged sentence
i = 1

for sentence in brown.tagged_sents():
	for (token, tag) in sentence:
		if i < 6:		
			print(token, tag)
		fd.inc(tag)
		cfd[token].inc(tag)
		i += 1

### the most frequent tag:
print fd.max()

wordbins = []
for token in cfd.conditions():
	wordbins.append((cfd[token].B(), token))


### sort tuples by number of unique tags
wordbins.sort(reverse=True)
print wordbins[0:3]


### masculine pronouns
male = ['he', 'his', 'him', 'himself']
female = ['she', 'hers', 'her', 'herself']
n_male, n_female = 0, 0 

for m in male: 
	n_male += cfd[m].N()

for f in female:
	n_female += cfd[f].N()

print float(n_male)/n_female

n_ambigous = 0
for (ntags, token) in wordbins:
	if ntags > 1:
		n_ambigous += 1

### Number of tokens with more than a signle POS tag
print n_ambigous


### WORD ASSOCIATION 
from nltk.corpus import brown, stopwords
from nltk.probability import ConditionalFreqDist

cfd = ConditionalFreqDist()

stopwords_list = stopwords.words('english')

### define a fucntion that returns true if the input tag is some form of noun
def is_noun(tag):
	return tag.lower in ['nn', 'nns', 'nn$', 'nn-tl','nn+bez',
                       'nn+hvz', 'nns$','np','np$','mp+bez','nps',
                       'nps$', 'nr','np-tl','nrs','nr$']


### count nouns that occure whithin a window of size 10 ahead of other nouns
for sentence in brown.tagged_sents():
	for (index, tagtuple) in enumerate(sentence):
		(token, tag) = tagtuple
		token = token.lower()
		if token not in stopwords_list and is_noun(tag):
			window = sentence[index + 1: index + 10]
			for (window_token, window_tag) in window:
				window_token = window_token.lower()
				if window_token not in stopwords_list and is_noun(window_tag):
					cfd[token].inc(window_token)
					print 'Irasiau'

print cfd.keys()
print '-' * 100
print cfd['bread']
print cfd['man']
print cfd['man'].max




