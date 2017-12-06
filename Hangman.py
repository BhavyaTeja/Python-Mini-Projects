import urllib2
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = urllib2.urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()

word = random.choice(WORDS)

def inWord(letter, word):
    return letter in word

def timesInWord(letter, word):
    return word.count('letter')

letter = str(input('Enter a letter'))

print(inWord(letter, word))

