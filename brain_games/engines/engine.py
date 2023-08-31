#!/usr/bin/env python3
import random

def random_generator(): #for calculator, for even , for gcd . use inside while.
    random_num = random.randint(1,100)
    random_num_2 = random.randint(1,100)
    return random_num, random_num_2

def progression_random():
        progression_start = random.randint(1, 100)
        progression_step = random.randint(2, 33)
        progression_slice_step = random.randint(5, 10)
        progression_pop_step = random.randint(1,10)
        return progression_start, progression_step, progression_slice_step, progression_pop_step
#math group

def check_even_num(number): # even
    return number % 2 == 0

def addition(number, number_2): #calculator
    return number + number_2

def subtraction(number, number_2):#calculator
    return number - number_2

def multiplication(number, number_2):#calculator
    return number * number_2

def gcd(a, b):
    # Проверяем, если одно из чисел равно нулю,
    # то НОД равен другому числу
    if b == 0:
        return a
    
    # Используем рекурсию, чтобы найти НОД
    # между b и остатком от деления a на b
    return gcd(b, a % b)

#User response group
def get_user_response(): #allfiles
    return input()

def print_question(number): #allfiles
    print('Question: ' + str(number))

def print_correct_answer(): #allfiles
    print('Correct!')


#follow functions work with username

def print_wrong_answer(answer, input_data,): #for even |
    if get_user_response == "yes":
        print(f"'{answer}' is the wrong answer. Correct answer was 'yes'.\nLet's try again, "+input_data+"!")
    else:
        print(f"'{answer}' is the wrong answer. Correct answer was 'no'.\nLet's try again, "+input_data+"!")

def print_wrong_answer_calculation(answer, correct_answer, input_data): #for calculator
    get_user_response !=  print(f"'{answer}' is the wrong answer. Correct answer was '{correct_answer}'. \nLet's try again, "+input_data+"!")
        
def congratulation(input_data):
    print("Congratulations, "+input_data+"!")
"""answer variable is what user gave into input. 
Correct answer is taken from functions(def subtraction,multiplication,addition) 
In iteration we meet it when it goes to print_wrong_answer_calculation(user_response, expected_result)
where expected result == correct_answer
"""
