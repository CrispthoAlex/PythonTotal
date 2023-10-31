from random import *
player = input("Type your name|> ")
total_rounds = 8
rounds = total_rounds

welcome = f"Welcome {player},\n"
rounds_text = (f"You have {rounds} rounds to find "
               f"the secret number between 1 and 100\n")
secret_number = 0

outside_range = "Number outside range. Chose another\n"
number_less = "Your number is less than secret number\n"
number_greater = "Your number is greater than secret number\n"

win_player = "Great, you did it. Your intents were "
play_again = ""

game_over = "Sorry, you are failed\n"
bye_player = f"Bye {player}\n"

while rounds > 0:
    if rounds == total_rounds:
        print(welcome)
        print(rounds_text)
        secret_number = randint(1, 101)
    shoot = int(input("Type your number |> "))
    win = False
    if 0 > shoot or shoot > 100:
        print(outside_range)
    elif shoot < secret_number:
        print(number_less)
    elif shoot > secret_number:
        print(number_greater)
    else:
        win = True
        print(f"{win_player} {total_rounds - rounds + 1}\n")

    rounds -= 1

    if rounds == 0:
        print(f"{game_over} "
              f"Secret number => {secret_number}\n")
    elif not win:
        print((f"You have {rounds} rounds to find "
               f"the secret number between 1 and 100\n"))
        continue

    while play_again not in ["y", "n"]:
        if win or rounds == 0:
            play_again = input("Play again? (y / n) ")
        else:
            pass
    if play_again == "n":
        print(bye_player)
        rounds = 0
        break
    elif play_again == "y":
        rounds = total_rounds
    play_again = ""

