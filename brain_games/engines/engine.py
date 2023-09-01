import random


def random_generator():
    random_num = random.randint(1, 100)
    random_num_2 = random.randint(1, 100)
    return random_num, random_num_2


def progression_random():
    start = random.randint(1, 100)
    step = random.randint(2, 33)
    slice_step = random.randint(5, 10)
    pop_step = random.randint(1, 10)
    return start, step, slice_step, pop_step


def check_even_num(number):  # even
    return number % 2 == 0


def addition(number, number_2):  # calculator
    return number + number_2


def subtraction(number, number_2):  # calculator
    return number - number_2


def multiplication(number, number_2):  # calculator
    return number * number_2


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def is_prime_logic(number):
    if number <= 1:
        return "no"
    if number == 2:
        return "yes"
    for i in range(2, number):
        if number % i == 0:
            return "no"
    return "yes"


def play_round(start, step, slice_step, pop_step):
    progression = list(range(start, 999, step))
    sliced_progression = progression[0:slice_step+1]

    if pop_step > slice_step:
        pop_step = slice_step

    progression_pop = sliced_progression.pop(pop_step)
    sliced_progression.insert(pop_step, '..')
    final_progression = ' '.join(map(str, sliced_progression))
    print_question(f"{final_progression}")

    user_response = get_user_response()
    print('Your answer:', user_response)

    return str(user_response), progression_pop


def get_user_response():  # allfiles
    return input()


def print_question(number):  # allfiles
    print('Question: ' + str(number))


def print_correct_answer():  # allfiles
    print('Correct!')


def print_wrong_answer(answer, input_data,):  # for even
    if get_user_response == "yes":
        print(f"'{answer}' is the wrong answer. Correct answer was 'yes'."
              f"\nLet's try again, " + input_data + "!")
    else:
        print(f"'{answer}' is the wrong answer. Correct answer was 'no'."
              f"\nLet's try again, " + input_data + "!")


# for calculator
def print_wrong_answer_calculation(answer, correct_ans, input_data):
    get_user_response != print(
        f"'{answer}' is the wrong answer. Correct answer was '{correct_ans}'. "
        f"\nLet's try again, " + input_data + "!")


def congratulation(input_data):
    print("Congratulations, " + input_data + "!")
