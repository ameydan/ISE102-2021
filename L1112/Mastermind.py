import pprint
import random

def fill_color_scheme():
    colors = {'R': "Red", 'G': "Green", 'B': "Blue", 'K': "blacK", 'O': "Orange", 'W': "White", 'P': "Purple",
              'Y': "Yellow"}
    print("Available colors are listed below, please use prefix capital letters")
    pprint.pprint(colors)
    return colors


def get_config_from_user(colors):
    num_of_colors = len(colors) + 1
    while num_of_colors > len(colors):
        print("How many colors would you like to use in the game?")
        num_of_colors = int(input(""))
        if num_of_colors > len(colors):
            print("Sorry,", num_of_colors, "is bigger than number of available colors")

    print("How many digits should your guesses may contain?")
    num_of_digits = int(input(""))
    if num_of_digits <= num_of_colors:
        print("Would you prefer repeated colors in your guesses? (Y/N)")
        repeat = True if input("").upper() == "Y" else False
    else:
        print("Colors would repeat in your case!!!")
        repeat = True

    selected_colors = {}
    for color in list(colors.keys())[:num_of_colors]:
        selected_colors[color] = colors[color]

    print("You will be playing over the following colors:")
    pprint.pprint(selected_colors)

    return selected_colors, num_of_digits, repeat


def make_random_arr(selected_colors, num_of_digits, repeat):
    arrangement = []

    if repeat:
        for i in range(num_of_digits):
            arrangement.append(random.choice(list(selected_colors.keys())))
    else:
        arrangement += list(selected_colors.keys())
        random.shuffle(arrangement)
        arrangement = arrangement[:num_of_digits]

    return arrangement


def get_guess_from_user():
    pass


def evaluate_guess():
    pass


def record_user_perf():
    pass


def display_score_table():
    pass


def mastermind_game():
    print("============= Welcome to Mastermind Game!!!!===================")
    colors = fill_color_scheme()
    selected_colors, num_of_digits, repeat = get_config_from_user(colors)
    #while True:
    print("Beginning game...")
    make_random_arr(selected_colors, num_of_digits, repeat)

    '''
    #Loop until correct guess
    get_guess_from_user()
    evaluate_guess()
    ###
    record_user_perf()
    display_score_table()
    ###
    '''
