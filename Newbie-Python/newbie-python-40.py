import random

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       === ''']

word = input()

def getRandomWord(wordList):

    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLettes, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed letters:", end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = "_ " * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLettes:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):

    while True:
        print(" Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in 'abcdefgijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print("Do you  want to play again (yes or no)")
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetter = " "
correctLetters = " "
secretWord = getRandomWord(word)

while True:
    displayBoard(missedLetter, correctLetters, secretWord)

    guess = getGuess(missedLetter + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True 
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetter = missedLetter + guess

        if len(missedLetter) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetter, correctLetters, secretWord)
            gameIsDone = True
            print('You have run out of guesses! \nAfter ' + str(len(missedLetter)) + " missed guesses and " + str(len(correctLetters) + ' correct guesses, the word was "' + secretWord + '"')

        if gameIsDone:



