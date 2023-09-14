# !/usr/bin/env python3
from brain_games.games.engine import start_game, gcd_t
from brain_games.games.brain_gcd_logic import generate_gcd_question


def main():
    start_game(generate_gcd_question,gcd_t)


if __name__ == '__main__':
    main()