decision1 = 10 > 9
if decision1:
    print("Correct")
else:
    print("Wrong data")

decision2 = 5 == 5.1
if decision2:
    print("Correct")
else:
    print("Wrong data")

decision3 = "hamster"
pet1 = "gato"
pet2 = "dog"
if decision3 == pet1:
    print("You have a cat")
elif decision3 == pet2:
    print("You have a dog")
else:
    print(f"{decision3} is an wrong pet")

age_user = int(input("Type your age (number): "))
age_limit = 18
age_max = 55
gender = input("Type your gender [female or man]").lower()

if age_user >= age_max:
    print("This is not your party")
elif age_user < age_limit:
    print("You don't have permission to enter.")
else:
    print("Almost in...\n")
    if gender == "female":
        print("You can enter.\nWelcome to the party")
    else:
        print("Only female, sorry")
