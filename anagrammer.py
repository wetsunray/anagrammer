"""
doob's Anagrammer

Dictionary taken from http://thepixiepit.co.uk/scrabble/CSW12.txt

Please input an answer:

An answer of "!q" will quit the dictionary.
An answer of "!qwc" will do a Quick Word Check
An answer of "!wsw" will find Words Starting With string
An answer of "!wew" will find Words Ending With string
An answer of "!wc" will find Words Containing letters

Note: A-Z only. No numbers, spaces, or special characters.

"""

##NOTE: 
##I took the dictionary from http://thepixiepit.co.uk/scrabble/CSW12.txt
##and renamed to wordlist.txt
##
##(I also deleted the first line instead of having to deal with that introductory
##'All CSW2012 (COLLINS) dictionary words with definitions.')
##

import re

wordlist = []

with open("Dictionary.txt",'r') as f:
    for line in f:
        if len(line) != 0:
            wordlist.append(line.split()[0])

def quick_word_check(input):
    return input.upper() in wordlist

def words_starting_with(input):
    list_of_words = []
    for word in wordlist:
        if re.match("^"+input.upper()+".*", word):
            list_of_words.append(word)
    return list_of_words

def words_ending_with(input):
    list_of_words = []
    for word in wordlist:
        if re.match(".*" + input.upper() + "$", word):
            list_of_words.append(word)
    return list_of_words

def words_containing(input):
    list_of_words = []
    for word in wordlist:
        if re.search(input.upper(), word):
            list_of_words.append(word)
    return list_of_words

def welcome():
    print (__doc__)

def main():
    welcome()
    answer = ''
    chk = ans = False
    while not chk:
        answer = raw_input("What is your answer?: ")
        if answer.lower() == '!q':
            break
        if answer.lower() == '!qwc':
            the_word = raw_input("What is the word you want to check?: ")
            if quick_word_check(the_word):
                print ("The word is valid.")
                continue
            else:
                print ("The word is invalid.")
                continue
        if answer.lower() == '!wsw':
            the_string = raw_input("What is the string you want to check?: ")
            print (words_starting_with(the_string))
            continue
        if answer.lower() == '!wew':
            the_string = raw_input("What is the string you want to check?: ")
            print (words_ending_with(the_string))
            continue
        if answer.lower() == '!wc':
            the_string = raw_input("What is the string you want to check?: ")
            print (words_containing(the_string))
            continue
    print ("Thank you! Goodbye.")
