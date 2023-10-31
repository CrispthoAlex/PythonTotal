from random import *

# short stick game

# initial list
sticks_option = ["---", "------", "---", "-", "------"]


# mix stick fn
def mix_sticks(stick_lists):
    """
    Shuffle the stick list
    :param stick_lists: stick list to be chose for the player
    :return: stick list shuffled
    """
    shuffle(stick_lists)
    return stick_lists


def test_luck():
    """
    Player chose a stick
    :return: number of stick choose
    """
    intent = ''
    intent_list = ["1", "2", "3", "4", "5"]
    while intent not in intent_list:
        intent = input("Chose a number from 1 to the 5 |> ")

    return int(intent)


# check intent
def check_intent(stick_list, intent):
    idx = intent - 1
    if stick_list[idx] == '-':
        print("You will wash dishes")
    else:
        print("Uff, you can breathe")

    print(f"You choose {stick_list[idx]}")


sticks_mixed = mix_sticks(sticks_option)
option_selected = test_luck()
check_intent(sticks_mixed, option_selected)


def reducir_lista(list1):

    list_temp = list(set(list1))

    n_max = max(list_temp)
    list_temp.remove(n_max)
    print(list_temp)
    return list_temp


lista_numeros = [4, 10, 9, 5, 11, 5, 4]

reducir_lista(lista_numeros)


def prom_list(new_list):
    sum = 0
    for n in new_list:
        sum += n
    return sum / len(new_list)


def lanzar_moneda():
    cara_cruz = ["Cara", "Cruz"]
    return choice(cara_cruz)


def probar_suerte(c_c, lista):
    if c_c == "Cara":
        print("La lista se autodestruirá")
        return []
    elif c_c == "Cruz":
        print("La lista fue salvada")
        return lista


lista_numeros = [98, 7, 64, 56, 78, 12, 3, 41, 2, 34]
probar_suerte(lanzar_moneda(), lista_numeros)
