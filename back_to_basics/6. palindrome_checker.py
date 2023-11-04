# PALINDROME checker

forward = input("Please enter a word: ")
forward = forward.lower()                      # make all text lower-case to avoid mismatch due to case sensitivity
backward = ""
counter = 1
for i in forward:
    back_slice = forward[-counter]              # slice out a single character at a time from the end of the word
    backward = backward + back_slice            # append these sliced characters to a new cariable to create backwards version of word
    counter += 1     
    #print(backward + " " + str(counter))       # Used as a control line to check code.

if forward == backward:
    print("Congrats! This is a palindrome")
else:
    print("Soz, try again")