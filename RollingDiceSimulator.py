#importing the random library

import random

#defining the function for generating the random variables

def dice():
    b = random.randint(1,6)
    print('\nThe number the dice produced is', b)

print('You want the Dice to be rolled? ')
choice = input('\nPlease enter your choice: Yes/No - ')
if choice == 'Yes' or choice == 'yes':
    choice = True
else:
    choice = False

while(choice):
        dice()
        choice = input("Do you want the dice to be rolled again? Enter your choice: Yes/No - ")
        if choice == 'Yes' or choice == 'yes':
            choice = True
        else:
            choice = False





