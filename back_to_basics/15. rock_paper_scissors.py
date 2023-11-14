# Rock Paper Scissors game

import random
import time

options = {1:"Rock", 2:"Paper", 3:"Scissors"}


def intro():
    global user_choice_num
    user_choice_num = 0
    while user_choice_num not in range(1,4):
        user_choice_num = int(input("""\nPlease choose your fighter: 
                1 - Rock
                2 - Paper
                3 - Scissors
                
                Please enter 1, 2 or 3  :   """))
        if user_choice_num not in range(1,4):
            print("\nI'm sorry, that is not a valid number. Try again.\n")
    return(user_choice_num)


def check_choice(num):
    global user_choice
    user_choice = options[user_choice_num]
    print(f"\nYou have chosen {user_choice}")
    print()
    return user_choice
       

def game_play(user, comp):

    if user == "Rock" and comp == "Scissors":
        print(f"Boom! {user} crushes {comp}!")
    elif user_choice == "Rock" and comp == "Paper":
        print(f"Oh no! {user} is covered by {comp}!")   
    elif user_choice == "Paper" and comp == "Rock":
        print(f"Boom! {user} covers {comp}!")
    elif user_choice == "Paper" and comp == "Scissors":
        print(f"Oh no! {user} is cut by {comp}!")   
    elif user_choice == "Scissors" and comp == "Rock":
        print(f"Oh no! {user} is crushed by {comp}!")
    elif user_choice == "Scissors" and comp == "Paper":
        print(f"Boom! {user} cuts {comp}!")
    else:
        print(f"An Impasse! {user_choice} meets {comp}!")   


def game_time():
    intro()
    check_choice(user_choice_num)
    time.sleep(2)
    print("Waiting for opponent's choice...\n")
    time.sleep(2)
    comp_rand_num = random.randint(1,3)
    computer_choice = options[comp_rand_num]
    game_play(user_choice, computer_choice)


#########################################################

#Main logic
game_time()
replay = input("\nWould you like to play again? Y/N  ")
if replay.upper() == "Y":
    game_time()
else:
    print("\nThanks for playing!")
    

