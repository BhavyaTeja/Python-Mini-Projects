import urllib2
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = urllib2.urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()
guess = []
count = 0

word = random.choice(WORDS)

def inWord(letter, word):
    return letter in word

def timesInWord(letter, word):
    return word.count('letter')

def getLetter():
    letter = str(input("Enter a letter"))
    if letter.isalpha() or len(letter) == 1:
        if inWord(letter, word) and timesInWord(letter, word) >= guess.count('letter'):
            guess.append('letter')
            if word[:len(guess)] == ''.join(guess):
                if len(word) == len(guess):
                    print('Congratulations! Your guess is correct, the word is ', word)
                else:
                    print('Good guess! Guess the next letter')
                    getLetter()
            else:
                print('Wrong guess! Try again')
                guess.pop()
                getLetter()
        else:
            print('The letter is already present or the letter is not there in the word! Try again')
            getLetter()
    else:
        print('Entered input has a number or it has more characters! Please try again')
        getLetter()

getLetter()
print(word)