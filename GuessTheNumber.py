import random

# create random number
randomNumber = random.randint(1,20)

# ask user their name
print("Hi! What is your name?")
userName = input()

# set guesses to 0 and ask user first guess
guessesMade = 0
print("Well " + userName + ", I'm thinking of a number between 1 and 20, can you guess it within 5 attempts?")
print("What's your first guess?")

# while loop is for each guess made
while guessesMade < 5:
    Try = int(input()) # guess is converted to integer for comparison statement
    guessesMade = guessesMade + 1
    if Try == randomNumber:
        break
    elif Try < randomNumber: # lets user create a smaller range to pick from
        print("Too Low!")
    elif Try > randomNumber: # even smaller range to pick from
        print("Too High!")

# tell user how many guesses they made whether correct or incorrect
if Try == randomNumber:
    guessesMade = str(guessesMade)
    print('Good job, ' + userName + '! You guessed my number in ' + guessesMade + ' guesses!')
if Try != randomNumber:
    randomNumber = str(randomNumber)
    print('Nope. The number I was thinking of was ' + randomNumber)