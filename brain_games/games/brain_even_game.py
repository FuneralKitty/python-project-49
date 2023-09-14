from random import randint


def play_game():
    quest = randint(0, 100)

    if quest % 2 == 0:
        operation = 'yes'
    elif quest % 2 != 0:
        operation = 'no'

    return quest, operation
