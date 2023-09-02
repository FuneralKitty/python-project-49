#!/usr/bin/env python3

from brain_games.engines.cli import welcome_user
from brain_games.engines.engine import (
    get_user_response,
    random_generator,
    addition,
    subtraction,
    multiplication,
    print_question,
    print_correct_answer,
    print_wrong_answer_calculation,
    congratulation
)


def play_game(operand, user_score, input_name):
    random_numbers = random_generator()
    random_num, random_num_2 = random_numbers
    print('What is the result of the expression?')

    if operand == '+':
        print_question(f"{random_num} + {random_num_2}")
        expected_result = addition(random_num, random_num_2)
    elif operand == '-':
        print_question(f"{random_num} - {random_num_2}")
        expected_result = subtraction(random_num, random_num_2)
    elif operand == '*':
        print_question(f"{random_num} * {random_num_2}")
        expected_result = multiplication(random_num, random_num_2)

    user_response = get_user_response()
    print('Your answer:', user_response)

    if user_response == str(expected_result):
        print_correct_answer()
        user_score += 1
    else:
        print_wrong_answer_calculation(
            user_response, expected_result, input_name)
        user_score = -1

    return user_score

def calculator():
    input_name = welcome_user()
    user_score = 0

    while user_score < 3:
        if user_score == -1:
            break
        
        if user_score < 1:
            user_score = play_game('+', user_score, input_name)
        
        if user_score < 2:
            user_score = play_game('-', user_score, input_name)
        
        if user_score < 3:
            user_score = play_game('*', user_score, input_name)
    
    if user_score == 3:
        congratulation(input_name)
