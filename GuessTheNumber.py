import random

# random number generated
randomNumber = random.randint(1,20)
userName = input("Hi! What is your name?: ")

guessesMade = 0
print("Well " + userName + ", I'm thinking of a number between 1 and 20, can you guess it within 5 attempts?")

# loop created so user only has 5 guesses
while guessesMade < 5:
    Try = int(input("What's your guess?: ")) 
    guessesMade = guessesMade + 1
    if Try == randomNumber: # loop stops and moves to code further down
        break
    elif Try < randomNumber: # lets user create a smaller range to pick from
        print("Too Low!")
    elif Try > randomNumber: # even smaller range to pick from
        print("Too High!")

# tell user how many guesses they made whether correct or incorrect
if Try == randomNumber:
    guessesMade = str(guessesMade)
    print('Good job, ' + userName + '! You guessed my number in ' + guessesMade + ' guesses!')
else:
    randomNumber = str(randomNumber)
    print('Unlucky! The number I was thinking of was ' + randomNumber)