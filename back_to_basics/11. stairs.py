# Print out a pyramid of numbers
storeys = input("Please enter a number: ")
storeys = int(storeys)

for i in range(1,storeys+1):
    display = str(i)           # Gotta turn this one into a string or it will just do a mathematical equation instead
    print(display * i)


