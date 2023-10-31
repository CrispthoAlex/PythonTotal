serie = "N-02"

"""if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("Don't exist this product")"""

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("Don't exist this product")

client = {
    "name": "Alex Gorev",
    "age": 53,
    "occupation": "astronaut"
}

movie = {
    "title": "Matrix",
    "technical_sheet": {
        "protagonist": "Keanu Reeves",
        "director": "Lana and Lilly Wachowski",
    }
}

elements = [client, movie, "book"]

for e in elements:
    match e:
        case {
            "name": name,
            "age": age,
            "occupation": occupation
        }:
            print("It's client")
            print(name, age, occupation)
        case {
            "title": title,
            "technical_sheet": {
                "protagonist": protagonist,
                "director": director
            }
        }:
            print("It's a movie")
            print(title, protagonist, director)
        case _:
            print("Unknown structure")
