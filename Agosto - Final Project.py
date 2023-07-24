# Genesis Agosto Summer 2023 Python Final Project
# Guess the Number Game
import random
import time
# Function for introductions
def intro():
    global user_name
    user_name = input("\nHello! Welcome to the Guess the Number Game!")
    print("Are you ready to guess the number?")

    
# Function to ask if they want to play
def want_play():
    answer = input("\nEnter YAY or NAY: ")
    if answer == "YAY":
        print("\nHooray! Let's play!")
        time.sleep(1)
    elif answer == "NAY":
        print("\nAwe, wrong answer. Let's play!")
    else:
        print("\nOops! Try again.")
        want_play()

       
# Function for game
def guess_number_game():
    number = random.randint(1, 10)
    guess = None
    while guess != number:
        guess = input("Guess a number between 1 and 10: ")
        guess = int(guess)
        if guess == number:
            print("\nCongratulations! You won!")
        elif guess != number:
            print("Oops! Wrong number, try again.")
        if not isinstance(guess, int):
            print("Guess must be an integer.")
            return 
              
# Function to ask the user to play again
def play_again():
    time.sleep(1)
    again = input("\nWould you like to play again? Enter YAY or NAY: ")
    if again == "YAY":
        print("\nHooray! Let's play again!")
        guess_number_game()
    elif again == "NAY":
        time.sleep(1)
        input("\nAwe, too bad. Press 7 to exit. Goodbye!")
        if again == "7":
            exit()
    else:
        print("\nOops! Try again.")
        play_again()
    if again not in ["YAY","NAY"]:
        print("Again, must be YAY or NAY.")
        return
        play_again()
    
# Section to begin the game
intro()
want_play()
guess_number_game()
play_again()
play_again()



        
