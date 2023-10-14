from random import randint


description = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_gcd_question():  # Измените имя функции
    first_gcd_num = randint(1, 100)
    second_gcd_num = randint(1, 100)
    answer = str(calculate_gcd(first_gcd_num, second_gcd_num))
    question = f'{first_gcd_num} {first_gcd_num}'

    return question, answer
