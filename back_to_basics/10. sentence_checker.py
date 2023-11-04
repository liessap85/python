# Enter a sentence and a word to be checked/counted

sentence = input("Hi, please enter a sentence: ")
word = input("Please enter the word for which you would like to search: ")
sentence = sentence.lower()               # make the sentence lower-case so that the word will always be found, regardless
word = word.lower()                       # same with word - case insensitive
times = 0

split = sentence.split(" ")

for i in split:
    if i == word:
        times += 1

if times > 0:
    print(f"\nCongrats, the word '{word}' appears in the sentence we checked {times} times.\n")
else:
    print(f"\nI'm sorry, the word '{word}' is not in that sentence, please try again.\n")