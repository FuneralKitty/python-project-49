import random
from brain_games.games.cli import welcome_user
from brain_games.games.engine import (
    congratulation,
    get_user_response,
    print_question,
    print_correct_answer,
    print_wrong_answer,
)


def check_even_num(number):  # even
    return number % 2 == 0


def play_game():
    input_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    user_score = 0

    while user_score < 3:
        name = input_name
        random_num = random.randint(1, 100)
        print_question(random_num)
        user_response = get_user_response()
        print('Your answer:', user_response)

        if check_even_num(random_num) and user_response == "yes":
            print_correct_answer()
            user_score += 1
        elif not check_even_num(random_num) and user_response == "no":
            print_correct_answer()
            user_score += 1
        else:
            print_wrong_answer(user_response, name)
            break

        if user_score == 3:
            congratulation(name)
