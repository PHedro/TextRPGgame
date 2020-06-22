import time

player = ["name_ph", 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "pronoun_ph", 0, [0, 0, 0, 0, 0, 0]]
# [name 0, lvl 1, inventory 2, pronoun to be called 3
# difficulty 4, stats 5]

answer_dict = {
    "yes": ("yeah", "yep", "sure", "okey-dokey", "alright", "fine", "absolutely", "yah"),
    "no": ("nope", "nah", "naw", "nae", "never", "no way"),
    "male": ("man", "men", "boy", "masculine"),
    "female": ("woman", "women", "girl", "feminine"),
    "much": ("a lot", "huge amount", "a huge amount", "lots")
}


def main_menu():
    answer = ""
    while answer != 'd':
        print_slow(
            "### -- Welcome to a_Game -- ###\n\n"
            "(a)New Game\t(b)Load Game\n(c)Options\t(d)Terminate Game\n\n"
            "### -- Welcome to a_Game -- ###\n")
        answer = input("Your action: ")
        answer.lower()
        if answer == 'a':
            new_game()
        elif answer == 'b':
            break  # something
        elif answer == 'c':
            break  # something
        elif answer == 'd':
            print("\nThe End\n")
            return 0


def new_game():
    difficulty = "ERROR"
    print_slow("Hmm, I see... you're new around here aren't you?\n"
               "It's okay, you'll get the hang of it.\n"
               "Well, so... what's your name?\n")
    answer1 = input("Your answer: ")
    if does_player_exist(answer1) == 1:
        print_slow("Hey! You're already in the game, do you want to log in to this char?\n")
        answer2 = input("Your answer: ")
        i = 0
        while i == 0:
            if answer2 == "yes":
                load_game(answer1)
                i += 1

            elif answer2 == "no":
                print_slow("Okay, so what's gonna be your new name?\n")
                answer = input("Your answer: ")
                if does_player_exist(answer) == 1:
                    print_slow("You think you\'re funny huh\n"
                               "OKAY " + answer.upper() + ", YOU SON OF A BITCH\nLET\'S GET THIS GOING\n")
                    load_game(answer)
                    player[4] = 4
                    game()
                    return
                load_game(answer2)
                i += 1

    elif does_player_exist(answer1) == 0:
        player[0] = answer1
        player[1] = 1
        i = 0
        while i == 0:
            print_slow("It seems you're not here alone like everyone else,\n"
                       "that\'s odd...\nBut ok, let\'s get you started:\n"
                       "Do you identify as a common gender?\n")
            answer = input("Your answer: ")
            answer.lower()
            if answer == "yes":
                print_slow("Umm, duh, the real question was: what is it, moron?\n")
                answer = input("Your answer")
                answer.lower()
            if answer == "male":
                player[3] = "he"
                print_slow("Oh yeah?\nTHEN FUCK YOU, DAMN CHAUVINIST\n"
                           "Well umm anyway, do you have any experience with RPGs?\n")
                i += 1
                difficulty = input("Your answer: ")
                difficulty.lower()
            elif answer == "female":
                player[3] = "she"
                print_slow("Okay, let\'s get you started.\n"
                           "Do you have any experience in RPGs?\n")
                i += 1

                difficulty = input("Your answer: ")
                difficulty.lower()
            elif answer == "no":
                print_slow("Okay, then let's-----------\n"
                           "Wait, what? What do you mean no?\n...\n...\n"
                           "You're weird\n"
                           "Anyway. Do you have any experience with RPGs?\n")
                i += 1

                difficulty = input("Your answer: ")
                difficulty.lower()
        i = 0
        while i == 0:
            if difficulty == "yes":
                print_slow("Okay, but how much?\n")
                answer = input("Your answer: ")
                answer.lower()
                if answer == "much":
                    player[4] = 3
                    print_slow("Okay, okay, smartass, you'll regret that, but okay.\n")
                    i += 1
                elif answer == "not much":
                    player[4] = 2
                    print_slow("Going for the middle path, yeah?\n"
                               "Remember: you are not Gandhi, you will die\n")
                    i += 1
                elif answer == "a little":
                    player[4] = 1
                    print_slow("Okie dokie, newbie. You\'ll fit right in\n")
                    i += 1
            elif difficulty == "no":
                print_slow("Oh, a true newcomer? How refreshing!\n")


# TODO Finish character creation from difficulty setting part


def print_slow(str1):  # Works exactly as the print function, except it does it slowly
    for letter in str1:
        print(letter, end='')
        time.sleep(.03)


def load_game(name):  # TODO LOAD GAME
    print("I would load now the game on the name of " + name + " but there really is no function yet so... sorry")


def does_player_exist(player_name):  # TODO FILE FUNCTIONS
    if player_name == "fred":
        return 1
    else:
        return 0


def game():
    print_slow("Now this would be the actual game, still working on it\n")
    return


main_menu()
