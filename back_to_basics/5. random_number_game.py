# Create a random number guesser
from random import randint

def game_play():
    chosen_num = randint(1,20)
    counter = 1

    guess = int(input("\nI'm thinking of a whole number between 1 and 20, what's your guess?   "))

    while (counter <=4 and guess != chosen_num):
        counter+=1
        if guess > chosen_num:
            guess = int(input("I'm sorry, try a lower number, you have " + str(5-(counter-1)) + " attempts remaining:   "))
        else:
            guess = int(input("I'm sorry, try a higher number, you have " + str(5-(counter-1)) + " attempts remaining:   "))
                
    if guess == chosen_num:
        print("\n\nWowza, nailed it! " + str(guess) + " is my number!\n")
    else:
        print("\nI'm sorry, you've run out of attempts!\n")

    global repeat
    repeat = input("Wanna play again? Y/N   " )

 #########################################################################################       

print("\nHi, welcome to the Random Number Game! \n All you have to do is correctly guess the number I have chosen. \n")

game_play()

while repeat.lower() == "y":
    game_play()
else:
    print("Thanks for playing!\n")












#This is when I tried to add in a counter adna  for loop

#  counter = 1

#     while counter<= 5:
#         while guess != chosen_num:
#             if guess > chosen_num:
#                 guess = int(input("I'm sorry, try a lower number, you have " + str(5-counter) + " attempts remaining:   "))
#                 (counter+1)
#             else:
#                 guess = int(input("I'm sorry, try a higher number, you have " + str(5-counter) + " attempts remaining:   "))
#                 (counter+1)

#         if guess == chosen_num:
#             print("\n\nWowza, nailed it! " + str(guess) + " is my number!\n")






# This is when I tried to have each section including a try block as functions - could not pass "local variable guess" into them

#def your_guess():
#     global guess 
#     guess = (input("\nI'm thinking of a whole number between 1 and 50, what's your guess?   "))

# def try_block():
#     try:
#         1 <= int(guess) >= 50
#     except ValueError:
#         guess = int(input("Please enter a valid whole number between 1 & 50:  "))

# def game_play():
#     while guess != chosen_num:
#         guess = int(input("I'm sorry, that wasn't correct, try again   "))
#         try_block()
#     if guess == chosen_num:
#         print("\n\nWowza, nailed it! " + str(guess) + " is my number!\n")

# def whole_game():
#    # your_guess()
#     try_block()
#     game_play()


    


        


   # while guess != chosen_num:
    
    #     guess = int(input("\nI'm thinking of a whole number between 1 and 50, what's your guess?   "))
    #     if guess < chosen_num:
    #         goes = attempt + 1
    #         print(f"I'm sorry, try a higher number, this will be guess number {goes} of 5:   ")
    #     elif guess > chosen_num:
    #         goes = attempt + 1
    #         print(f"I'm sorry, try a lower number, this will be guess number {attempt} {goes} of 5:   ")
    #     else:
    #         print("\n\nWowza, nailed it! " + str(guess) + " is my number!\n")
    #    # if attempt > 
    #     #   break
           
    # print("I'm sorry, you've run out of attempts!\n")

    #else:
    #
    # print("I'm sorry, you've run out of attempts!\n")
