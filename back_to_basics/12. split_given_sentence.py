# Take an input sentence and split each chatacter into a list         
#Simplest way is using the unpack option  -   

string = input("Please enter the sentence you would like to split: ")
print([*string])

# #Also tried a for loop
# list=[]
# for char in string:
#   list.append(char)
#  print(list)

# # Tried to use re.split, but couldn't get it not to add a white space at the beginning
#re.split(r'/W*'+, string)

# Couldn't use string.split() on this one as there is no set delimeter


