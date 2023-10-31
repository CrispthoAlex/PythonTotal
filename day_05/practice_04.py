def contar_primos(n_prime):
    """
    Show on screen the prime numbers in the range from 0 to n_prime
    (include), and return prime numbers count
    Ex:
        print(contar_primos(12))
        # 5
    :param n_prime: Number given
    :return:
    - A count of prime numbers
    """
    count = 0
    if n_prime <= 1:
        return count

    for n in range(2, n_prime + 1):
        if n in [2, 3, 5, 7]:
            count += 1
        elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            pass
        else:
            count += 1
    return count

print(contar_primos(50))