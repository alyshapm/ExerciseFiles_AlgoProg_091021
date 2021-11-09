import os

def countWords(bookContents): # counts word from text and switches it into dictionary
    bookContents = bookContents.lower() # turns text into lowercase
    punc = '''!()-[];:'"\,<>./?@#$%^&*_~''' 
    for char in bookContents: 
        if char in punc:
            bookContents = bookContents.replace(char, "") # removes punctuation and replaces it with null
    wordFrequency = {} # declares empty dictionary
    splitWords = bookContents.split() # splits text into words
    for word in splitWords:
        wordFrequency[word] = wordFrequency.get(word,0)+1 # counts the frequency of each word, which will be the value
    return wordFrequency
        
os.chdir("/Users/alyshapm/Desktop/BINUS/Algorithm and Programming/SEM 1/Complete notes") # determines location of file
book = open("info.txt", "r") 
bookContents = book.read() # turns text into str, in which it will go through the countWords function

finalWordCount = countWords(bookContents) # now the text is translated into dictionary

liHapax = [] # declare new list for the hapax
for key, value in finalWordCount.items():
    if value == 1: # if value in dict equals to 1, then the key, or word, will be appended into the liHapax
        liHapax.append(key)

print(liHapax)
