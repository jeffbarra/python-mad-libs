# open up the txt file and read ("r") 
with open("story.txt", "r") as f:
    story = f.read()

# create a set of words
words = set()

# start of word 
start_of_word = -1

# targets
target_start = "<"
target_end = ">"


for i, char in enumerate(story): 
    # if char is equal to the "<"
    if char == target_start:
         # mark start of word as "i"
        start_of_word = i
    
    # find the end of the word
    if char == target_end and start_of_word != -1:
        # slice the word within the angle brackets
        word = story[start_of_word: i + 1]
        # add to or word set
        words.add(word)
        # reset start of word
        start_of_word = -1

# generate answer
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

# replace words with the words that the user provided 
for word in words:
    story = story.replace(word, answers[word])


print(story)

