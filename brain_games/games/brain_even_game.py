from random import randint


QUEST = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    quest = randint(0, 100)

    if quest % 2 == 0:
        operation = 'yes'
    elif quest % 2 != 0:
        operation = 'no'

    return quest, operation
