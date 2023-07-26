# Genesis Agosto Summer 2023 Python Final Project
# Criminal Procedure Amendment Review Game
import random
import time
from pprint import pformat

# Introduction 
print("Hello! Welcome to the Criminal Procedure Amendment Review Game!")
time.sleep(2)

print("The purpose of this review game to help you refresh your memory on the Amendments covered in Criminal Procedure.")
time.sleep(2)

# Rules 
print("The rules of the game are simple.")
time.sleep(2)

print("I will provide a description of an Amendment related to Criminal Procedure.")
time.sleep(2)

print("You will then type in the number (i.e., 4th, 5th, 6th, or 8th) of the Amendment that matches the description.")
time.sleep(3)

print("If you guess correctly, then you get a point.")
time.sleep(2)
print("If not, you get zero points.")
time.sleep(2)

# Variables
name = input("Please enter your name: ")
score = 0

# Prompt before questions
input("Hi, " + name + " ,are you ready for this knowledge refresh?") 
time.sleep(1)
print("-----------------------")
print("Here are the questions:")
print("-----------------------")
time.sleep(2)

# List of questions
q1 = "This Amendment secures the 'right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.' Which Amendment is it?"
q2 = "This Amendment states that 'private property be taken for public use, without just compensation.' Which Amendement is it?"
q3 = "This Amendment ensures the right to an attorney in criminal procceedings. Which Amendment is it?"
q4 = "This Amendment states that no warrants will be issued without probable cause and supoorted by Oath or affirmation.' Which Amendment is it?"
q5 = "This Amendment requires that no cruel and unusual punishments inflicted. Which Amendment is it?"
q6 = "This Amendment ensures that 'the accused shall enjoy the right to a speedy and public trial, by an impartial jury of the State and district wherein the crime shall have been committed.' Which Amendment is it?"
q7 = "This Amendment states that no 'person be subject for the same offence to be twice' nor 'be deprived of life, liberty, or property, without due process of law.' Which Amendment is it?"

# Dictionary of questions with corresponding answers
questions = {q1:"4th", q2:"5th", q3:"6th", q4:"4th", q5:"8th", q6:"6th", q7:"5th"}

# Running the game again
def again():
    again = input("Would you like to try again?: (y/n)")
    if again == 'y':
        for i in questions:
            score = 0
            print(i)
            print("-----------------------")
            ans = input("Enter your answer: ")
            if ans == questions[i]:
                print("\nGreat job,",name,"!")
                score = score+1
                print("Current score: ",score)
                print("-----------------------")
            elif ans != questions[i]:
                print("\nNope, the correct answer is", questions[i])
                score = score+0
                print("Current score: ",score)
                print("-----------------------")
    else:
        print("Final score is:", score)
        print("Goodbye!")
        sys.exit()
    if again not in ['y','n']:
        print("Again, must be y or n.")
        return
        again()
     
# Review game
attempts = None
for i in questions:
    random.choice(dict(questions.items()))
    print(i)
    print("-----------------------")
    ans = input("Enter your answer: ")
    if ans == questions[i]:
            print("\nGreat job,",name,"!")
            score = score+1
            print("Current score: ",score)
            print("-----------------------")
    elif ans != questions[i]:
            print("\nNope, the correct answer is", questions[i])
            score = score+0
            print("Current score: ",score)
            print("-----------------------")

print("Your final score is: ", score)
again()
        
