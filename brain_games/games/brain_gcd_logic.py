import random
from brain_games.games.cli import welcome_user
from brain_games.games.engine import (
    congratulation,
    get_user_response,
    print_question,
    print_correct_answer,
    print_wrong_answer_calculation,
)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def random_generator():
    random_num = random.randint(1, 100)
    random_num_2 = random.randint(1, 100)
    return random_num, random_num_2


def play_game():
    input_name = welcome_user()
    user_score = 0

    print('Find the greatest common divisor of given numbers.')

    for _ in range(3):
        if user_score < 3:
            random_numbers = random_generator()
            random_num, random_num_2 = random_numbers
            print_question(f"{random_num} {random_num_2}")

            user_response = get_user_response()
            print('Your answer:', user_response)
            result = gcd(random_num_2, random_num)

            if user_response == str(result):
                print_correct_answer()
                user_score += 1
            else:
                print_wrong_answer_calculation(
                    user_response, result, input_name)
                break

    if user_score == 3:
        congratulation(input_name)
