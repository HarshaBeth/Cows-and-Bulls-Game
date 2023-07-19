import random

newNumber = ""

guess = ""

cows = 0
bulls = 0
nCows = 0
nBulls = 0
skipPosition = []

falseInput = True
tries = 0
checkNumCounter = 10

def checkCows(guess, newNumber):
    cows = 0

    for i in range(4):
        if (guess[i] == newNumber[i]):
            cows += 1
            skipPosition.append(i)

    return cows


def checkBulls(guess, newNumber):
    bulls = 0

    for i in range(4):
        for j in range(4):
            if(guess[i] == newNumber[j]) and (guess[i] != newNumber[i]):
                bulls += 1

    return bulls


def checkRepetitions(checkNumCounter):

    while(checkNumCounter > 4):
        newNumber = str(random.randint(1000, 9999))
        checkNumCounter = 0

        for i in range(len(newNumber)):
            for j in range(len(newNumber)):
                if(newNumber[i] == newNumber[j]):
                    checkNumCounter += 1

    return newNumber


newNumber = checkRepetitions(checkNumCounter)


print("Welcome to the Cows and Bulls Game!")
print("Enter a number:")

while(guess != newNumber):

    while(falseInput):
        guess = input(">>> ")

        if(guess.isdigit() == False):
            print("Not a number")
        elif(len(guess) < 4) or (len(guess) > 4):
            print("Number entered must be 4 digits")
        else:
            falseInput = False

    falseInput = True

    nCows = checkCows(guess, newNumber)
    nBulls = checkBulls(guess, newNumber)
    print(f"{nCows} cows, {nBulls} bulls")

    tries += 1


print(f"Congrats, you took {tries} tries")
