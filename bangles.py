import random
def getSecretNum(numDigits):
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum
def getClues(guess,secretnum):
    if guess == secretNum:
        return 'You got it!'
    clue = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
        else:
            clue.append('None')
    return ' '.join(clue)
def isOnlyDigits(num):
    if num == "":
        return True
    for i in num:
        if i not in ["0,1,2,3,4,5,6,7,8,9"]:
            return True
def playAgain():
    play = input("Do you want to play again? Yes or No?") 
    return play.startswith('y')  
NUMDIGITS = 3
MAXGUESS = 10
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')
while True:
    secretNum = getSecretNum(NUMDIGITS)
    print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
    numGuesses = 1
    while numGuesses < MAXGUESS:
        print( 'Guess' + str(numGuesses))
        guess = input("Guess Again")
        clue = getClues(guess, secretNum)
        print(clue)
        if guess == secretNum:
            break
        numGuesses+=1
        if numGuesses == MAXGUESS:
            print ('You ran out of guesses. The answer was ' + secretNum)
            break
    if playAgain() == True:
        continue
    else:
        break