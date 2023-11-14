# Sum of dictionary values

my_dict={
    "Hannah" : 22,
    "Richard" : 44,
    "Claire" : 49,
    "Donna" : 18,
    "TM": "Devon"
    }

# This is the short elegant answer, but it will not handle str values
#print(sum(my_dict.values()))


# I tried to throw a spanner in, by trying to weed out non-int values.
# the number classes come back as int but will not sum - realised why - I had chose "sum" as the name of the variable, which is dumb because it is a built-in - doh!
# Added the try except block with a continue command as it was previously getting stuck on string value.
total = 0

for v in my_dict.values():
    try:
        value = int(v)
    except ValueError:
        continue
    print(type(v))
    total = (total + v)
print(total)

