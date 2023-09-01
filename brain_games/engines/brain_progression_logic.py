from brain_games.engines.cli import welcome_user
from brain_games.engines.engine import (
    congratulation,
    print_correct_answer,
    print_wrong_answer_calculation,
    progression_random,
    play_round
)


def play_game():
    input_name = welcome_user()
    user_score = 0
    print('What number is missing in the progression?')
    while user_score < 3:
        random_numbers = progression_random()
        start, step, slice_step, pop_step = random_numbers
        user_response, expected_result = play_round(
            start, step, slice_step, pop_step)

        if user_response == str(expected_result):
            print_correct_answer()
            user_score += 1
        else:
            print_wrong_answer_calculation(
                user_response, expected_result, input_name)
            break

    if user_score == 3:
        congratulation(input_name)


if __name__ == '__main__':
    play_game()
