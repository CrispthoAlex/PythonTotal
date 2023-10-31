coins = 15
while coins > 0:
    print(coins)
    coins -= 1
else:
    print("Reload your purse :(")

respond = "y"
while respond == "y":
    respond = input("Continue? (y/n)")
    if respond != "y":
        if respond != "n":
            print("Just use 'y' or 'n'")
            respond = "y"
else:
    print("Ok. Bye")

while respond == "y":
    pass
print("test pass")

