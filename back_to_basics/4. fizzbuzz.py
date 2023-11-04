number = int(input("Please enter a whole number between 1 and 250 to play FizzBuzz:  "))

try:
    if number not in range(1,250):
        raise ValueError()              
except ValueError:
    print("Sorry, please enter a valid full number between 1 and 250")
else:
    for x in range(1,(number+1)):       # remember, the final number in a range is not included by default, so add +1
        fizz = (x % 3)
        buzz = (x % 5)
        if (fizz == 0) and (buzz == 0):
            print("FizzBuzz")
        elif fizz == 0:
            print("Fizz")
        elif buzz == 0:
            print("Buzz")
        else:
            print(x)




