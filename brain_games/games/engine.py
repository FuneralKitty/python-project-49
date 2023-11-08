from brain_games.games.cli import welcome_user
from brain_games.games.constants import game_rounds


def start_game(game_function, description):
    print('Welcome to the Brain Games!')
    input_name = welcome_user()
    user_score = 0

    print(description)
    while user_score < game_rounds:
        quest, operation = game_function()
        print('Question:', quest)
        answer = input('Your answer: ')

        if operation == answer:
            print('Correct!')
            user_score += 1
        else:
            print(f"'{answer}' is the wrong answer."
                  f"Correct answer was '{operation}'."
                  f"\nLet's try again, " + input_name + "!")
            break

    if user_score == game_rounds:
        print('Congratulations, ' + input_name + '!')
