import time 
import random



clearConsole = lambda: print('\n'*15)

clearConsole()
print("Welcome to Simon Says!\nRed circular light = 1, red square light = 2, green circular light = 3.\nPress enter to start.")
input()

pastNumbers = []
round = -1
lose = 0

while lose == 0:

    round = round + 1

    nextNumber = random.randint(1, 3)
    pastNumbers.append(nextNumber)
    
    for i in range (len(pastNumbers)):
        clearConsole()
        print(pastNumbers[i])
        time.sleep(1.5)
        clearConsole()
        time.sleep(0.3)
    
    for i in range(len(pastNumbers)):
        userInput = int(input())
        if userInput != pastNumbers[i]:
            lose = 1
            break
        clearConsole()

clearConsole()
print("Incorrect.\nYou made it to round {}.".format(round))

