import random
from brain_games.engines.cli import welcome_user
from brain_games.engines.engine import (
    congratulation,
    get_user_response,
    print_question,
    print_correct_answer,
    print_wrong_answer_calculation,
    progression_random,
)

def play_round(input_name, start, step, slice_step, pop_step):
    print('What number is missing in the progression?')
    progression = list(range(start, 999, step))
    sliced_progression = progression[0:slice_step+1]

    if pop_step > slice_step:
        pop_step = slice_step

    progression_pop = sliced_progression.pop(pop_step) #число которое нужно найти
    sliced_progression.insert(pop_step, '..')
    final_progression = ' '.join(map(str, sliced_progression))# Вывод всей прогрессии
    print_question(f"{final_progression}")

    user_response = get_user_response()
    print('Your answer:', user_response)
    
    return int(user_response), progression_pop

def play_game():
    input_name = welcome_user()
    user_score = 0
    while user_score < 3:
        random_numbers = progression_random()
        start, step, slice_step, pop_step = random_numbers
        user_response, expected_result = play_round(input_name, start, step, slice_step, pop_step)

        if user_response == expected_result:
            print_correct_answer()
            user_score += 1
        else:
            print_wrong_answer_calculation(user_response, expected_result, input_name)
            break

    if user_score == 3:
        congratulation(input_name)

if __name__ == '__main__':
    play_game()
