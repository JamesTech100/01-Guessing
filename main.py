import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# Number Guessing Game!

playingGame = True

while playingGame == True:
    takenGuesses = 0

    randNumber = random.randint(1,50)
    print('I am thinking of a number between 1 and 50')
    print('you have 5 chances to guess the number')

    while takenGuesses < 5:
        print('Take a guess')
        guess = input()
        guess = int(guess)

        takenGuesses = takenGuesses + 1

        if guess == 27:
            print('that is my favorite number!')

        if guess > randNumber:
            print('your guess is a bit too high')

        if guess < randNumber:
            print('your guess is a bit too low')

        if guess == randNumber:
            break

    if guess == randNumber:
        takenGuesses = str(takenGuesses)
        print('Nice! it took you ' + takenGuesses + ' tries to guess that the number was ' + randNumber + '!')

    if guess != randNumber:
        randNumber = str(randNumber)
        print('The correct number was ' + randNumber)
    
    print('press enter to play again')
    yesno = input()
