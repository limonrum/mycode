#!/usr/bin/env python3
"""Jurassic Park Trivia | Solution with While True Loops"""

# Question 1
attempts = 0
while True:
    question1 = input("In Jurassic Park, what kind of dinosaur is the star attraction? ")
    if question1.lower() == "t-rex":
        print("Correct! The T-Rex is the star attraction!")
        break
    else:
        print("Sorry, that's not correct.")
        attempts += 1
    if attempts == 3:
        print("The correct answer is T-Rex.")
        break

# Question 2
attempts = 0
while True:
    question2 = input("What type of DNA was used to fill the gaps in the dinosaur genome? ")
    if question2.lower() == "frog":
        print("Correct! Frog DNA was used to fill the gaps in the genome!")
        break
    else:
        print("Sorry, that's not correct.")
        attempts += 1
    if attempts == 3:
        print("The correct answer is Frog.")
        break

