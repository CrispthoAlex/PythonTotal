# import numbers module
import numbers


# functions
def ask_service():
    print(f"""
    {'#' * 40}
    WELCOME TO PYTHON PHARMACY
    {'#' * 40}
    
    """)
    option = '-1'
    while int(option) not in range(0, 4):
        print("""
        Please, select your service:
        [1] Perfume
        [2] Pharmacy
        [3] Cosmetics
        [0] Exit
        """)
        service_word = ''
        try:
            option = input('|> ')
            nb_service = int(option)
            if nb_service == 1:
                service_word = 'perfume'
            elif nb_service == 2:
                service_word = 'pharmacy'
            elif nb_service == 3:
                service_word = 'cosmetics'
            elif nb_service == 0:
                print('... Closing program ...')
                break
        except ValueError:
            print('Invalid option')
            option = '-1'
        if int(option) not in range(0, 4):
            numbers.shift_text_decorator(service_word)


def shift_program():
    while True:
        ask_service()
        try:
            another_shift = input('Do you want another shift? [Y] / [N]').upper()
            ['Y', 'N'].index(another_shift)
        except ValueError:
            print('Invalid option')
        else:
            if another_shift == 'N':
                print('Thanks for your visit')
                break


shift_program()


