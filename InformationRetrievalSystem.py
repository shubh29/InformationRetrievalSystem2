'''
Created on Sun Oct 25 12:41:47 2015

@authors: 
            Max Levine
            Shubham Mahajan
'''
################################## Sources ####################################
# https://github.com/shubh29/Postinglist/blob/master/PostingList.py
# http://www.nltk.org/book/ch02.html
# https://docs.python.org/3/library/collections.html

################################## Imports ####################################

import nltk
import os
import math
import re
import operator
from collections import *


################################## Storage ####################################

documentTerms = {}

length = {}

scores = {}

postingsList = {}


################################## Methods ####################################

# Get stop words
stopwords = nltk.corpus.stopwords.words('english')

# Read the documents from the directory and collect vocabulary
def collectVocab():
    for file in os.listdir(os.getcwd()):
         if file.endswith(".txt"):
              fileOpen = open(file,'r')
              fileRead = fileOpen.read()
              documentTerms[file] = [w.lower() for w in nltk.word_tokenize(fileRead) if w.lower() not in stopwords and re.compile(r'^[a-z]+$').search(w.lower()) is not None]
              # Get # of terms in a document
              length[file] = len(set([w.lower() for w in nltk.word_tokenize(fileRead) if w.lower() not in stopwords and re.compile(r'^[a-z]+$').search(w.lower()) is not None]))
collectVocab()

# Get query and break it into terms
inputQuery = input('Please enter the Query: ')
queryTerms = set([w.lower() for w in nltk.word_tokenize(inputQuery)])

def postingListOperation():
    for term in queryTerms:
        postingsList[term] = {}
postingListOperation()        

# Get postings (doc, tf)
for term in queryTerms:
	for doc in documentTerms:
		count = 0
		for dTerm in documentTerms[doc]:
			if term == dTerm:
				count = count + 1
		if count > 0:
			postingsList[term][doc] = count

for l in length:
	scores[l] = 0

# For the terms present in document (if any), generate a score for that document
def computeTermFrequency():
    for term in postingsList:
        if len(postingsList[term]) != 0:
            idf = math.log10(len(length)/len(postingsList[term]))
            for d in postingsList[term]:
                scores[d] += postingsList[term][d] * idf
computeTermFrequency()

for d in length:
	scores[d] = scores[d]/length[d]

# Generate the output of documents based on terms occurance
def generateOutput():
    documentSortedInOrder = OrderedDict(sorted(scores.items(), key=operator.itemgetter(1), reverse=True))
    print("Matching Documents:")
    for document in documentSortedInOrder:
        if documentSortedInOrder[document] != 0:
            print(document)
generateOutput()

################################ End of File ##################################