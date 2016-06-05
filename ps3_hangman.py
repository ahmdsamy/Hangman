# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "E:\pyhton course\my codes\week 2/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    right=0
    for letter in secretWord:
         if lettersGuessed.count(letter)>0:
             right+=1
        
    if right==len(secretWord) :
        return True
    else : 
          return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    mystring=''
    for letter in secretWord:
           if lettersGuessed.count(letter)>0:
               mystring+=letter
           else:
               mystring+='_'
    return str(mystring)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    remainingletter=string.ascii_lowercase
    mystring=string.ascii_lowercase 
    for letter in mystring:
          if lettersGuessed.count(letter)>0:
             remainingletter = remainingletter.replace(letter, "")    
    return remainingletter   
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    '''secretWord='''
    
    lettersGuessed=''
    y=8
    x=len(secretWord)
    computerguess= ''
    mokarar=''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " +str(x)+ " letters long."
    print "-------------"
    while y>0:
        print "You have " +str(y)+ " guesses left."
        print "Available letters:", 
        print getAvailableLetters(lettersGuessed)
        u=raw_input("Please guess a letter: ") 
        uInLowerCase = u.lower()
        
        lettersGuessed+=uInLowerCase
        mokarar=lettersGuessed.count(uInLowerCase)
        if mokarar>1:
               print"Oops! You've already guessed that letter: ",
               print getGuessedWord(secretWord, lettersGuessed)
               
        elif uInLowerCase in str(secretWord):
           print "Good guess: ", 
           print getGuessedWord(secretWord, lettersGuessed)
           computerguess= getGuessedWord(secretWord, lettersGuessed)
           if "_" not in str(computerguess) :
               print "-------------" 
               print"Congratulations, you won!"  
               break  
        else : 
           print "Oops! That letter is not in my word: ",
           print getGuessedWord(secretWord, lettersGuessed)
           y-=1
        print "-------------"  
        
        if y==0:
           print "Sorry, you ran out of guesses. The word was " +str(secretWord) + "."                    
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
