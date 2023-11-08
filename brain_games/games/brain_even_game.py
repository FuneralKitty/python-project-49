from random import randint
from brain_games.games.constants import first_number_even, second_number_even

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    generated_num_for_question = randint(first_number_even, second_number_even)

    def is_even():
        nonlocal generated_num_for_question
        return True if generated_num_for_question % 2 == 0 else False

    if is_even():
        operation = 'yes'
    else:
        operation = 'no'

    return generated_num_for_question, operation
