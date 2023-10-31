def adding():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    print(num1 + num2)
    print("Thanks for adding with python" + num1)


try:
    adding()
except TypeError:
    # print("Something was wrong")
    print("Trying to concatenate different types")
except ValueError:
    print("That's not a number")
else:
    print("You did it")
finally:
    print("That's all")


def take_number():

    while True:
        try:
            num1 = int(input("Type a number: "))
        except:
            print("That's not a number")
        else:
            print(f"You type a number {num1}")
            break
    print("Thank you")


take_number()
