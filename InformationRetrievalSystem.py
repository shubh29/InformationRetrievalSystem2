# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:24:47 2015

@author: Shubham
Max
"""

from TwitterSearch import *

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['owl','eagles']) # let's define all words we would like to have a look for
    tso.set_language('en')# we want to see tweets from english only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key ='7ovlnQDliiKXTkQSrVr5hKHgq',
        consumer_secret = 'WFTzfGhu8veWgm08rqywkJWR4lYXVZzGQOQ4Kb1MUElhezPCea',
        access_token = '3631252332-8Y6J9vXNlvGCvR4rNysCD5YtIk811NIWOYI16R6',
        access_token_secret = 'LrZiv6h8lyRU0L8vfHbFQKVUTmZr4jACpzU9ReAYKkG9B'
     )
     
     #testestest

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        tweetString = tweet['user']['screen_name'], tweet['text'] 
        #print(tweetString)
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

def writeToTextFile():
    print('Writing a new text file\n')
    #Name of text file coerced with .txt
    textFileName = 'doc5.txt'
    
    try:
        #Trying to create a new file or open one
        writeToTextFile = open(textFileName, "w")
        for tweet in ts.search_tweets_iterable(tso):
            writeToTextFile.write(str(tweetString))
        writeToTextFile.close()
        print('File writing completed!\n')
    except:
        print('Something went wrong while writing to the file!')
        #quit python
        sys.exit(0)
writeToTextFile()