#!/usr/bin/env python3
import random
import sys
import time
incorrect = 0
guesslist = []
print("Welcome! Your goal is to guess the random number.")
time.sleep(1.0)
print("What is the range you want? For example, if you want 1-50, type 50.")
print("Select the range.")
while True:
 try:
     rg = int(input("<<< "))
     break
 except ValueError:
     print("Type it as a number. For example, 5 instead of five.")
print(f"Okay, the range is 1-{rg}")
number = random.randint(1,rg)
time.sleep(1.0)
print("Guess the number...")
while True:
 try:
     guess = int(input("<<< "))
 except ValueError:
     print("Type it as a number. For example, 5 instead of five.")
     continue
 if guess in guesslist:
     print("You already guessed that number.")
 guesslist.append(guess)
 if guess == number:
        print("Correct! You win! Exiting...")
        sys.exit()
 else:
     print("Try again...")
     incorrect += 1
     if incorrect == 10:
         print("It has been 10 incorrect guesses.")
     elif incorrect == 20:
         print("It has been 20 incorrect guesses.")
     elif incorrect == 30:
         print("It has been 30 incorrect guesses.")
     elif incorrect == 40:
         print("It has been 40 incorrect guesses.")
     elif incorrect == 50:
         print("It has been 50 incorrect guesses...I give up on counting!")
     


