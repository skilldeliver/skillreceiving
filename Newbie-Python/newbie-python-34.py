# This is a "Guess the Number" game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20."
      + " You have six guesses.")

for guessesTaken in range(6):
    
    Taken = str(guessesTaken + 1)
    print("Take your " + Taken + " guess.")
    
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    elif guess == number:
        break

if guess == number:
    guesses = str(guessesTaken + 1)
    print('Good job ' + myName + '! You guessed my number in ' + guesses +
          "guesses!")
elif guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")






