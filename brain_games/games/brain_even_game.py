from random import randint


description = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_game():
    generated_num_for_question = randint(0, 100)
    def is_even():
        nonlocal generated_num_for_question
        if generated_num_for_question % 2 == 0:
            return True
    if is_even():
        operation = 'yes'
    else:
        operation = 'no'

    return generated_num_for_question, operation
