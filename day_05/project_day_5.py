from random import choice
# Hangman game (Juego del ahorcado)

# choice secret word
secret_words = ["camaleon", "edificio", "ornitorrinco", "odontologia",
                "campanario", "amasar", "estadio", "acompañante",
                "cigarrillo", "amatista", "zafiro", "xilofono",
                "natividad", "cometa", "elevador", "computacion",
                "tecnologia", "sistemas"
                ]


def choice_secret_word(list_word):
    """
    Choice a word from a list of words

    :return: word choiced
    """
    return choice(list_word)


# player inputs letter
def player_selection():
    """
    Receive a letter from the player, and return it
    :return: input letter from the player
    """
    ltr = ""
    while ltr in ["", "\n", " "]:
        ltr = input("Please select a letter |> ")
    return ltr.lower()


# try win the game
def try_win(secret_word):
    try_option = ""
    while try_option not in ["y", "n"]:
        try_option = input("Do you want try to win? (y / n) ")
        if try_option == "n":
            return False
    player_word = input("Type your word |> ")
    player_word.lower()
    secret_word.lower()
    if player_word == secret_word:
        return True
    else:
        print(f"'{player_word}' is not the secret word\n")
        return False


def show_letter_in_sec_word(sec_word, ltr_found, show_ltr):
    """
    Print on screen the letters found in the secret word.
    :param sec_word: secret word
    :param ltr_found: letters found by the player
    :param show_ltr: building secret word
    """
    count = 0
    show_temp = [ltr for ltr in show_ltr]

    while count < len(sec_word):
        if "_" == show_temp[count] and ltr_found == sec_word[count]:
            show_temp[count] = ltr_found
        count += 1
    show_temp = "".join(show_temp)
    return show_temp


# check letter in secret word
def checking_ltr(secret_word, ltr_player):
    """
    Take the letter of player, check if letter is into the secret word until
    player
    :param secret_word: word selected by the system
    :param ltr_player: letter selected by the player
    :return:
        -
    """
    # check_count = 0
    check_limit = len(secret_word) - 2
    secret_w = secret_word[::]
    show_word = "_" * len(secret_word)
    letter_found = 0
    text_endgame = f"the secret word is '{secret_w}'\n"
    ltr_set = set()
    win = False

    while check_limit >= 1:
        if ltr_player in ltr_set:
            print(f"Letter {ltr_player} choiced before\n")
        elif ltr_player not in secret_w:
            print(f"'{ltr_player}' not in secret word\n")
            check_limit -= 1
            print(f"You have {check_limit} opportunities left\n")
        else:
            ltr_set.add(ltr_player)
            print(f"'{ltr_player}' in secret word\nYour letters are:"
                  f"\n{ltr_set}\n")
            # return view letters on secret word
            show_word = show_letter_in_sec_word(secret_w, ltr_player, show_word)
            print(f"Secret word:\n{show_word}\n")
            letter_found += 1
        if show_word == secret_w:
            win = not win
            break

        # try win the game
        if ((int(len(secret_w) / 2) < letter_found) and try_win(secret_word) and
                not show_word == secret_w):
            win = not win  # turn on True
            break
        if check_limit != 0:
            ltr_player = player_selection()

    if letter_found <= len(secret_w) and win:
        print(f"You win, {text_endgame}")
        return True
    else:
        print(f"You lose, {text_endgame}")
        return False


# player win or lose
def hangman_game():
    """
    Hangman game:
    The game will choice a secret word from a words list. The user will type
    a letter trying to find the secret word. It could try to win
    typing the secret word
    :return: True if user wins, else False
    """
    player_name = ""
    result = True
    play_again = ""
    print("Welcome to Hangman game\n")
    while result:
        if player_name == "":
            player_name = input("Type your name |> ")
        play_again = ""
        print(f"Hi {player_name}\n")
        print("""INSTRUCTIONS:\n
        1) The game will choice a secret word
        2) Player types a letter to find the secret word
        2.1) If letter is not in secret word, player lose a life (opportunity)
        \t* Life (opportunity) number will be iqual to the length of secret word less two letters
        Ex: hospital has 8 letter, so you have 6 lives (opportunities)
        2.2) Player could try to type the secret word to win, just when the number
        of found letters are less or equal than secret word half.
        3) Player wins when all letters are found, or when player types the secret word
        """)

        result = checking_ltr(choice_secret_word(secret_words), player_selection())
        if result:
            print(f"Congrats {player_name} for winning")
        else:
            print(f"Sorry {player_name}")
        while play_again not in ["y", "n"]:
            play_again = input("Do you want play again? (y / n)")
            if play_again == "n":
                result = False


hangman_game()
