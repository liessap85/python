# Enter two numbers and find which is bigger
try:
    first_number=float(input("Hi, please enter your first number: "))
    second_number=float(input("Please enter your second number: "))
except ValueError:
    print("You have not entered a number")
else:
    if first_number > second_number:
        print("The first number is greater than the second number")
    elif second_number > first_number:
        print("The second number is greater than the first number")
    else:
        print("The numbers are the same")
