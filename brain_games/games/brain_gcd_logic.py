from random import randint
from brain_games.games.constants import first_number_gcd, second_number_gcd

description = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_gcd_question():
    first_gcd_num = randint(first_number_gcd, second_number_gcd)
    second_gcd_num = randint(first_number_gcd, second_number_gcd)
    answer = str(calculate_gcd(first_gcd_num, second_gcd_num))
    question = f'{first_gcd_num} {second_gcd_num}'

    return question, answer
