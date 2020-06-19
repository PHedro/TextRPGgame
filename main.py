import time


def mainMenu():
    answer = ""
    while answer != 'd':
        print_slow("### -- Welcome to a_Game -- ###\n(a)New Game\t(b)Load Game\n(c)Options\t(d)Terminate Game\n")
        answer = input("Your action: ")
        if answer == 'a':
            newGame()
        elif answer == 'b':
            break #something else
        elif answer == 'c':
            break #something else else
        elif answer == 'd':
            return 0

def newGame():
    print("")


def print_slow(str):
    for letter in str:
        print(letter, end='')
        time.sleep(.1)


mainMenu()
