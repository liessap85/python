# Write a short program to give a letter grade according to numberical score.

import time

num_score = input("\n Hi, What is your score? ")
try:
    score = int(num_score)
    print("Calculating, please wait... \n")
    time.sleep(3)
except ValueError:
    print("Please enter a valid whole number between 1 and 100")
else:
    if score > 100:
        print("I'm sorry, please enter a valid whole number between 1 and 100")
    elif score >= 90:
        print("Congrats, you have achieved an A\n")
    elif score >=80:
        print("Well done, you have achieved a B\n")
    elif score >=70:
        print("Good job, you have achieved a C\n")
    elif score >=60:
        print("Nice try, you have achieved a D\n")
    else:
        print("I'm sorry, you have not achieved a passing grade. F\n")


