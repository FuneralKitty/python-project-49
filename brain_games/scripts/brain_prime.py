# !/usr/bin/env python3
from brain_games.games.engine import start_game, prime
from brain_games.games.brain_prime_logic import play_game


def main():
    start_game(play_game, prime)


if __name__ == '__main__':
    main()
