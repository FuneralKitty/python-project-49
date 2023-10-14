# !/usr/bin/env python3
from brain_games.games.engine import start_game
from brain_games.games.brain_gcd_logic import generate_gcd_question,description


def main():
    start_game(generate_gcd_question,description)


if __name__ == '__main__':
    main()
