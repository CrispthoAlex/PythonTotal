def str_transform(word):
    """
    Take a string as input, return a list of
    unique letters sorted alphabetically
    Ex:
        print(str_transform("alphabetically"))
        # ['a', 'b', 'c', 'e', 'h', 'i', 'l', 'p', 't', 'y']
    :param word: text to handle
    :return:
        - All unique letters in the form of a list,
        arranged alphabetically.
    """
    text_list = list(set([ch for ch in word]))
    text_list.sort()
    return text_list
