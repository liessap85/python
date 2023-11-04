# Given a random input, count the number of alphabetical, numeric and symbolic characters.

chars = 0
digits = 0
symbols = 0

string = input("Please input a random mix of characters; letters, numbers and special characters (all are permitted): ")

print(f"\nYour chosen string is {len(string)} characters long")

for i in string:
    if i.isalpha():
        chars += 1
    elif i.isnumeric():
        digits += 1
    else:
        symbols += 1

print(f"\nTotal number of alphabetical characters in your string: {chars}")
print(f"Total number of numerical characters in your string: {digits}")
print(f"Total number of symbolic characters in your string: {symbols}\nPlease note, in this program, a space or tab counts as a symbol.\n")
