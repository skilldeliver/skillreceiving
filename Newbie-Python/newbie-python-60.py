import random

MAX_DIGITS = 3
GUESS = 10

def giveRandomNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    
    secretNum = ''
    for i in range(MAX_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def giveClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(MAX_DIGITS)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        if guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)



def checkValidation(num):

    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def printing():
    print("I am thinking of a %s-digit number. Try to guess what it is." % (MAX_DIGITS))
    print('The clues I give are...')
    print('When i say:    That means:')
    print(' Bagels        None of the digits is correct.')
    print(' Pico          One digit is correct but in the wrong position.')
    print(' Fermi         One digit is correct and in the right position.')

while True: 
    printing()
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' % (MAX_GUESS))

    guessesTaken = 1 
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s:' % (guessesTaken))
            guess = input()

        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' % (secretNum))

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break

