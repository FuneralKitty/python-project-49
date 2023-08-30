#!/usr/bin/env python3
import random

def random_generator(): #for calculator, for even use inside while.
    random_num = random.randint(1,100)
    random_num_2 = random.randint(1,100)
    return random_num, random_num_2

def check_even_num(number): # even
    return number % 2 == 0

def addition(number, number_2): #calculator
    return number + number_2

def subtraction(number, number_2):#calculator
    return number - number_2

def multiplication(number, number_2):#calculator
    return number * number_2

def get_user_response(): #allfiles
    return input()

def print_question(number): #allfiles
    print('Question: ', number)

def print_correct_answer(): #allfiles
    print('Correct!')

def print_wrong_answer(answer): #for even
    if get_user_response == "yes":
        print(f"'{answer}' is the wrong answer. Correct answer was 'yes'.\nnoLet's try again !")
    else:
        print(f"'{answer}' is the wrong answer. Correct answer was 'no'.\nLet's try again !")

def print_wrong_answer_calculation(answer, correct_answer): #for calculator
    print(f"'{answer}' is the wrong answer. Correct answer was '{correct_answer}'. Let's try again!")
"""answer variable is what user gave into input. 
Correct answer is taken from functions(def subtraction,multiplication,addition) 
In iteration we meet it when it goes to print_wrong_answer_calculation(user_response, expected_result)
where expected result == correct_answer
"""
