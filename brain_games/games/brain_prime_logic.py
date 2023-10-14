import random


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    question = random.randint(2, 100)
    n = 0

    for i in range(2, question // 1):
        if question % i == 0:
            n = n + 1
    if n <= 0:
        result = True
    else:
        result = False
    return result, question


def play_game():
    result, quest = is_prime()

    if result is True:
        operation = 'yes'
    elif result is False:
        operation = 'no'

    return quest, operation
