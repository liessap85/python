# Remove unnecessary spaces from a paragraph
paragraph = "Argentina  wins   football   world cup 2022 in a nail biting final match that led to a       spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most    memorable   matches."

split = paragraph.split(" ")

# print each item of the list "split" ONLY if it is not an empty space
for i in split:
    if i != "":
        print(i, end = " ")      # include a space after each printed item to maintain normal text