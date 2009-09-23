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

# sort the words by probability
words = []
for word in wordcount:
    words.append(word)

def compare_occurrence_count(word1, word2):
    if wordcount[word1] < wordcount[word2]:
        return 1
    elif wordcount[word1] == wordcount[word2]:
        return 0
    else:
        return -1

words.sort(compare_occurrence_count)
print(words[0:200])

