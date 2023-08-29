#!/usr/bin/env python3
import random
from brain_games.engines.engine import check_even_num,get_user_response,print_question,print_correct_answer,print_wrong_answer

def check_even_num(number):
    return number % 2 == 0

def get_user_response(): 
    return input()

def print_question(number):
    print('Question: ', number)

def print_correct_answer():
    print('Correct!')

def print_wrong_answer(answer):
    if get_user_response == "yes":
        print(f"'{answer}' is the wrong answer. Correct answer was 'yes'.\nnoLet's try again !")
    else:
        print(f"'{answer}' is the wrong answer. Correct answer was 'no'.\nLet's try again !")
def play_game():
    print('Answer "yes" if the number is even otherwise answer "no": ')
    user_score = 0 
    while user_score  < 3:
        random_num = random.randint(1,100)
        print_question(random_num)
        user_response = get_user_response()
        print('Your answer: ', user_response)

        if check_even_num(random_num) and user_response == "yes":
            print_correct_answer()
            user_score += 1
        elif not check_even_num(random_num) and user_response == "no":
            print_correct_answer()
            user_score += 1
        else:
            print_wrong_answer(user_response)
            break

    if user_score == 3:
        print("Congratulations!")
play_game()

