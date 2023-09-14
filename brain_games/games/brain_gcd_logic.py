from random import randint


def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_gcd_question():  # Измените имя функции
    random_num = randint(1, 100)
    random_num_2 = randint(1, 100)
    answer = str(calculate_gcd(random_num, random_num_2))
    question = f'{random_num_2} {random_num}'

    return question, answer
