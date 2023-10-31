# generators

def shift_perfume():
    """
    Generate a shift from the perfume service
    :return: shift service text
    """
    for pe in range(1, 1000):
        yield f'PE-{pe}'


def shift_pharmacy():
    """
    Generate a shift from the pharmacy service
    :return: shift service text
    """
    for ph in range(1, 1000):
        yield f'PH-{ph}'


def shift_cosmetics():
    """
    Generate a shift from the pharmacy service
    :return: shift service text
    """
    for co in range(1, 1000):
        yield f'CO-{co}'


# catching generators
pe_shift_text = shift_perfume()
ph_shift_text = shift_pharmacy()
co_shift_text = shift_cosmetics()


# decorator
def shift_text_decorator(word):
    """
    print shift text to indicate to the user
    :param word: shift generator
    :return:
    """
    print(f'{"#" * 40}\n')
    print('Your shift is:')
    if word == 'perfume':
        print(next(pe_shift_text))
    elif word == 'pharmacy':
        print(next(ph_shift_text))
    elif word == 'cosmetics':
        print(next(co_shift_text))
    print('Wait, you will be attended to soon\n')
    print(f'{"#" * 40}\n')
