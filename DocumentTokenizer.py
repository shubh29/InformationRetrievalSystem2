# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:41:03 2015

@author: User
"""

import nltk
import sys

def tokenizeTextDataDoc1():
    file_content = open("doc1.txt").read()
    tokens = nltk.word_tokenize(file_content)
    print(tokens)
    print('Writing a new text file\n')
    #Name of text file coerced with .txt
    textFileName = 'vocab.txt'
    
    
    try:
        #Trying to create a new file or open one
        writeToTextFile = open(textFileName, "w")
        writeToTextFile.write(str(tokens))
        writeToTextFile.close()
        print('File writing completed!\n')
    except:
        print('Something went wrong while writing to the file!')
        #quit python
        sys.exit(0)  
tokenizeTextDataDoc1()
