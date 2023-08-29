#!/usr/bin/env python3
"""def scripts():
    check_even_num
    get_user_response
    print_question
    print_correct_answer
    print_wrong_answer"""
import random

def check_even_num(number):
    return number % 2 == 0

def addition(number, number_2):
    return number + number_2

def subtraction(number, number_2):
    return number - number_2

def multiplication(number, number_2):
    return number * number_2

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