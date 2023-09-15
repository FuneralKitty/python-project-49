from brain_games.games.cli import welcome_user


def calc():
    return ('What is the result of the expression?')


def even():
    return ('Answer "yes" if the number is even, otherwise answer "no".')


def gcd_t():
    return ('Find the greatest common divisor of given numbers.')


def prime():
    return ('Answer "yes" if given number is prime. Otherwise answer "no".')


def progress():
    print('What number is missing in the progression?')


def start_game(game_function, func):
    print('Welcome to the Brain Games!')
    input_name = welcome_user()
    user_score = 0
    f = func()
    print(f)
    while user_score < 3:
        quest, operation = game_function()
        print("Question:", quest)
        answer = input('Your answer: ')

        if operation == answer:
            print('Correct!')
            user_score += 1
        else:
            print(f"'{answer}' is the wrong answer."
                  f"Correct answer was '{operation}'."
                  f"\nLet's try again, " + input_name + "!")
            break

    if user_score == 3:
        print("Congratulations, " + input_name + "!")
