##########################
# This program is an example of
# how to find the words that occur
# commonly in a textfile

# open the file for reading
f = file("/home/voel/Desktop/moby-dick.txt", "r")

# wordcount contains the number of occurences of each word
wordcount = {}
# the total number of words in the file
total_words = 0

# run through the file, reading one line at a time
for line in f:
    # line.split(), splits a string by whitespaces
    for word in line.split():
        # we are going to increase the number of
        # occurrences for the word, and to make that possible
        # we need to tell that words we haven't seen
        # has occured 0 times
        if not wordcount.has_key(word):
            wordcount[word] = 0
        wordcount[word] = wordcount[word] + 1
        total_words = total_words + 1

# Find the words that occur more often than one in a thousand
common_words = []
for word in wordcount:
    probability = float(wordcount[word])/total_words
    if probability > 0.001:
        common_words.append(word)

# show the common words in alphabetical order
common_words.sort()
print(common_words)

