import random  # import random module from python library

guessesTaken = 0  # Assign 0 to guessesTaken variable

print('Hello! What is your name?')  # call print function with 'Hello! What is your name?' parameter
myName = input()  # Assign input function to myName variable

number = random.randint(1, 20)  # Assign random.randint function with 1, 20 parameter to number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # call print function with the given string and myName variable

while guessesTaken < 6:  # iterate the inside block of code until the given condition(guessesTaken < 6) is true
    print('Take a guess.') # call print function with 'Take a guess.' parameter
    guess = input()  # Assign input function to guess variable
    guess = int(guess)  # convert guess variable into integer

    guessesTaken += 1  # add 1 to the value of guessesTaken variable

    if guess < number:  # with if statement check the given condition(guess < number) is true
        print('Your guess is too low.')  # call print function with ' Your guess is too low.' parameter

    if guess > number:  # with if statement check the given condition(guess > number) is true
        print('Your guess is too high.')  # call print function with 'Your guess is too high.' parameter

    if guess == number:  # with if statement check the given condition(guess == number) is true
        break  # with break statement terminate the current loop

if guess == number:  # with if statement check the given condition(guess == number) is true
    guessesTaken = str(guessesTaken)  # convert guessesTaken variable into string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # # call print function with the given string and number and guessesTaken variable

if guess != number:  # with if statement check the given condition(guess != number) is true
    number = str(number)  # convert number variable into string
    print('Nope. The number I was thinking of was ' + number)  # call print function with the given string and number variable
