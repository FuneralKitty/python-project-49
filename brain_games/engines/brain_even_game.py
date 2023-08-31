import random
from brain_games.engines.cli import welcome_user 
from brain_games.engines.engine import (
    check_even_num,
    congratulation,
    get_user_response,
    print_question,
    print_correct_answer,
    print_wrong_answer,
)


def play_game():
    input_name = welcome_user()
    print('Answer "yes" if the number is even otherwise answer "no": ')
    user_score = 0 
    while user_score  < 3:
        name = input_name
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
            print_wrong_answer(user_response, name) #1
            break
        if user_score == 3:
            congratulation(name)

            
""" #1 answer variable is what user gave into input. 
Correct answer is taken from functions(def subtraction,multiplication,addition) 
In iteration we meet it when it goes to print_wrong_answer_calculation(user_response, expected_result)
where expected result == correct_answer
"""

