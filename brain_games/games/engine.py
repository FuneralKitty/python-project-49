from brain_games.games.cli import welcome_user


def start_game(game_function,description ):
    print('Welcome to the Brain Games!')
    input_name = welcome_user()
    user_score = 0

    print(description)
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
