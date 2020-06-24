import time
from random import randint


def roll(dice_n):
    return randint(1, dice_n)


def roll_stat():
    dices = [roll(6), roll(6), roll(6), roll(6)]
    dices.sort()
    dices.remove(dices[0])
    return sum(dices)


# main player class
class Player:
    name = "place_holder",
    lvl = 0,
    inventory = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    noun = "it",
    stats = [0, 0, 0, 0, 0, 0],  # str, con, dex, int, wis, cha
    difficulty = 0


# pre prepared classes for those who do not want to bet
class PreMadeClasses:
    fighter = [17, 10, 14, 8, 12, 14]
    sorcerer = [8, 10, 14, 17, 14, 12],
    ranger = [12, 10, 17, 14, 14, 8],
    barbarian = [18, 16, 8, 5, 12, 8]
    diplomat = [10, 8, 14, 16, 15, 17]


p1 = Player()
npc_class = PreMadeClasses()

answer_dict = {
    "test": "TEST2",
    "yes": ("yeah", "yep", "sure", "okey-dokey", "alright", "fine", "absolutely", "yah"),
    "no": ("nope", "nah", "naw", "nae", "never", "no way", "not at all"),
    "male": ("man", "men", "boy", "masculine"),
    "female": ("woman", "women", "girl", "feminine"),
    "much": ("a lot", "huge amount", "a huge amount", "lots"),
    "not much": ("some", "well...", "considerable"),
    "a little": ("almost none", "you could say a little", "i regret my previous answer")
}


def main_menu():
    # while True:
    #   a = input("Entry TEST2: ")
    #   if check_answer("test", a):
    #       break
    answer = ""
    while answer != 'd':
        print_slow(
            "### -- Welcome to a_Game -- ###\n\n"
            "(a)New Game\t(b)Load Game\n(c)Options\t(d)Terminate Game\n\n"
            "### -- Welcome to a_Game -- ###\n")
        answer = input("Your action: ")
        answer = answer.lower()
        if answer == 'a':
            new_game()
        elif answer == 'b':
            load_game("fred")
            break  # something
        elif answer == 'c':
            break  # something
        elif answer == 'd':
            print("\nThe End\n")
            return 0

# new_game(): Starts a new game, proceding to checking if the character you're trying to create already exists
# or if not, creates it
# {UNFINISHED}


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
            if check_answer("yes", answer2):
                load_game(answer1)
                return

            elif check_answer("no", answer2):
                print_slow("Okay, so let\'s start over.")
                new_game()
    elif does_player_exist(answer1) == 0:
        p1.name = answer1
        p1.lvl = 1
        i = 0
        while i == 0:
            print_slow("It seems you're not here alone like everyone else,\n"
                       "that\'s odd...\nBut ok, let\'s get you started:\n"
                       "Do you identify as a common gender?\n")
            answer = input("Your answer: ")
            answer = answer.lower()
            print(answer)
            if check_answer("yes", answer):
                print_slow("Umm, duh, the real question was: what is it, moron?\n")
                answer = input("Your answer: ")
                answer = answer.lower()
            if check_answer("male", answer):
                p1.noun = "he"
                print_slow("Oh yeah?\nHow innovating......\n"
                           "Well umm anyway, do you have any experience with RPGs?\n")
                i += 1
                difficulty = input("Your answer: ")
                difficulty = difficulty.lower()
            elif check_answer("female", answer):
                p1.noun = "she"
                print_slow("Okay, let\'s get you started.\n"
                           "Do you have any experience in RPGs?\n")
                i += 1

                difficulty = input("Your answer: ")
                difficulty = difficulty.lower()
            elif check_answer("no", answer):
                print_slow("Okay, then let's-----------\n"
                           "Wait, what? What do you mean no?\n...\n...\n"
                           "You're weird\n"
                           "Anyway. Do you have any experience with RPGs?\n")
                i += 1

                difficulty = input("Your answer: ")
                difficulty = difficulty.lower()
        i = 0
        while i == 0:
            if check_answer("yes", difficulty):
                print_slow("Okay, but how much?\n")
                answer = input("Your answer: ")
                answer = answer.lower()
                if check_answer("much", answer):
                    p1.difficulty = 3
                    print_slow("Okay, okay, smartass, you'll regret that, but okay.\n")
                    i += 1
                elif check_answer("not much", answer):
                    p1.difficulty = 2
                    print_slow("Going for the middle path, yeah?\n"
                               "Remember: you are not Gandhi, you will die\n")
                    i += 1
                elif check_answer("a little", answer):
                    p1.difficulty = 1.5
                    print_slow("Okie dokie, newbie. You\'ll fit right in\n")
                    i += 1
            elif check_answer("no", difficulty):
                p1.difficulty = 1
                print_slow("Oh, a true newcomer? How refreshing!\n")

            print_slow("So, we have some pre-made classes, want to look at some?")
            while True:
                yn = input("Your answer: ")
                yn = yn.lower()
                if check_answer("yes", yn) or check_answer("no", yn):
                    break
                else:
                    print("I\'m sorry tha\'s not a valid response")
                    continue
            if check_answer("yes", yn):

                print_slow("There are a few:\n[Fighter] = The fighting specialized mercenary, nothing special\n"
                           "[Barbarian] = The innate fighter. None of them chose to start fighting,"
                           "they just did it. Their natural strength and relentless are stunning,"
                           "their intelligence though... not so much\n"
                           "[Sorcerer] = The one in a million born with magical treats in it\'s soul, "
                           "some say they are descendants of the celestial legends\n"
                           "[Ranger] = Those who secluded themselves from society and lived their lives in"
                           "the forest, their knowledge of their surroundings and their senses is truly "
                           "spectacular\n"
                           "[Diplomat] = Well these ones are quite special, quite... fragile. They decided"
                           "not to fight, well for most of the time, not really an easy task, to be honest.\n\n"
                           "So, interested in any of them?")
                while True:
                    yn2 = input("Your answer: ")
                    yn2 = yn2.lower()
                    if check_answer("yes", yn2) or check_answer("no", yn2):
                        break
                    else:
                        print("I\'m sorry tha\'s not a valid response")
                        continue
                if check_answer("yes", yn2):
                    print_slow("Okay, wich one?\n"
                               "[Fighter] - [Barbarian]\n"
                               "[Sorcerer] - [Ranger]\n"
                               "[Diplomat]")
                    while True:
                        job = input("Your answer: ")
                        job = job.lower()
                        if job == "barbarian" or job == "fighter" or job == "ranger" or job == "sorcerer" or job == "diplomat":
                            break
                        else:
                            print("I\'m sorry tha\'s not a valid response")
                            continue
                    if job == "barbarian":
                        p1.stats = npc_class.barbarian
                    elif job == "fighter":
                        p1.stats = npc_class.fighter
                    elif job == "ranger":
                        p1.stats = npc_class.ranger
                    elif job == "sorcerer":
                        p1.stats = npc_class.sorcerer
                    elif job == "diplomat":
                        p1.stats = npc_class.diplomat
                    print_slow("Hmm " + job + " OK\nI guess this is it, isn\'t it?\n"
                                              "Okay see you soon")
                elif check_answer("no", yn2):
                    print_slow("So... wanna take your chances with the dice?")
                    while True:
                        answer = input("Your answer: ")
                        answer = answer.lower()
                        if check_answer("yes", answer) or check_answer("no", answer):
                            break
                        else:
                            print("I\'m sorry tha\'s not a valid response")
                            continue
                    if check_answer("yes", answer):
                        while True:
                            print_slow("How do you like: ")
                            fullstats = [roll_stat(), roll_stat(), roll_stat(), roll_stat(), roll_stat(), roll_stat()]
                            print(fullstats)
                            print("Is it enough for you?")
                            statq = input("Your answer: ")
                            if check_answer("yes", statq):
                                p1.stats = fullstats.copy()
                            else:
                                continue
                            ###############################################################################################
                            # Still need to do the file part in order to finish the new_game(), due to the need of a save #
                            ###############################################################################################
                input("Press ENTER to see your profile")
                print(p1)
                return 0


# DONE difficulty, name, lvl, inv, stats
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


def check_answer(key, value):
    if value == key:
        return True
    else:
        for el in answer_dict[key]:
            if value == el:
                return True
    return False


def save_game():
    print("Not in the game yet")
    return


main_menu()
