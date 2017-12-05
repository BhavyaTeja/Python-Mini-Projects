#importing the libraries

import random

#Random function which generates the random numbers between 1 and 100

def rando():
    a = random.randint(1, 100)
    b = int(input('Guess the number between 1 and 100: '))
    compare(a,b)
    choice = input('You want to try again: Yes/No - ')
    if choice == 'Yes' or choice == 'yes':
        rando()

#Compare function compares the guessed number with the random number

def compare(a,b):
    if b > a:
        b = int(input('Wrong Guess! Enter a smaller number: '))
        compare(a,b)
    elif b < a:
        b = int(input('Wrong Guess! Enter a greater number: '))
        compare(a,b)
    else:
        print('Correct Guess')

rando()