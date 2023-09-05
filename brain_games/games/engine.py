def get_user_response():  # allfile
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
