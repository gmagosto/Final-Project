Python (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Genesis Agosto Summer 2023 Python Final Project
>>> # Guess the Number Game
>>> import random
>>> import time
>>> # Function for introductions
>>> def intro():
...     time.sleep(4)
...     global user_name
...     user_name = input("\nHello! Welcome to the Guess the Number Game!")
...     print(f"\nHello!\n")
...     time.sleep(2)
...     print("Are you ready to guess the number?")
...     time.sleep(2)
... 
...     
>>> # Function to ask if they want to play
>>> def want_play():
...     answer = input("\nEnter YAY or NAY: ")
...     if answer == "YAY":
...         print("\nHooray! Let's play!")
...     elif answer == "NAY":
...         print("\nAwe, wrong answer. Let's play!")
...     else:
...         print("\nOops! Try again.")
...         want_play()
... 
...         
>>> # Function for game
>>> def guess_number_game():
...     number = random.randint(1, 20)
...     guess = None
...     while guess != num:
...         guess = input("Guess a number between 1 and 20: ")
...         guess = int(guess)
...         if guess == num:
...             print("\nCongratulations! You won!")
...         else:
            print("Oops! Wrong number, try again.")

            
# Function to ask user to play again
def play_again():
    time.sleep(1)
    again = input("\nWould you like to play again? Enter YAY or NAY: ")
    if again == "YAY":
        print("\nHooray! Let's play again!")
        guess_number_game()
    elif again == "NAY":
        time.sleep(1)
        input("\nAwe, too bad. Press 7 to exit. Goodbye!")
    else:
        print("\nOops! Try again.")
        play_again()



        
