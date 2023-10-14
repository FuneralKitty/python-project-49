import random


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    prime_number = random.randint(2, 100)
    n = 0

    for i in range(2, prime_number // 1):
        if prime_number % i == 0:
            n = n + 1
    if n <= 0:
        result = True
    else:
        result = False
    return result, prime_number


def play_game():
    result, prime_number = is_prime()

    if result is True:
        operation = 'yes'
    elif result is False:
        operation = 'no'

    return prime_number, operation
