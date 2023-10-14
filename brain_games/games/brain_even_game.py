from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    generated_num_for_question = randint(0, 100)

    if generated_num_for_question % 2 == 0:
        operation = 'yes'
    elif generated_num_for_question % 2 != 0:
        operation = 'no'

    return generated_num_for_question, operation
