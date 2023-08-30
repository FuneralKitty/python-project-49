#!/usr/bin/env python3

import random
from brain_games.engines.engine import (
    get_user_response,
    random_generator,
    addition,
    subtraction,
    multiplication,
    print_question,
    print_correct_answer,
    print_wrong_answer_calculation
)

def calculator():
    user_score = 0 
    while user_score < 3:
        random_numbers = random_generator()
        random_num, random_num_2 = random_numbers
        print('What is the result of the expression?')
        if user_score == 0:
            print_question(f"{random_num} + {random_num_2}")
            user_response = get_user_response()
            print('Your answer:', user_response)
            expected_result = addition(random_num, random_num_2)
            if int(user_response) == expected_result:
                print_correct_answer()
                user_score += 1
            else:
                print_wrong_answer_calculation(user_response, expected_result)
                break
        elif user_score == 1:
            print_question(f"{random_num} - {random_num_2}")
            user_response = get_user_response()
            print('Your answer:', user_response)
            expected_result = subtraction(random_num, random_num_2)
            if int(user_response) == expected_result:
                print_correct_answer()
                user_score += 1
            else:
                print_wrong_answer_calculation(user_response, expected_result)
                break
        elif user_score == 2:
            print_question(f"{random_num} * {random_num_2}")
            user_response = get_user_response()
            print('Your answer:', user_response)
            expected_result = multiplication(random_num, random_num_2)
            if int(user_response) == expected_result:
                print_correct_answer()
                user_score += 1
            else:
                print_wrong_answer_calculation(user_response, expected_result)
                break
    if user_score == 3:
        print("Congratulations:", "!")

calculator()
s