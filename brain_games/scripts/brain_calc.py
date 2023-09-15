# !/usr/bin/env python3
from brain_games.games.engine import start_game, calc
from brain_games.games.brain_calculation import play_game


def main():
    start_game(play_game, calc)


if __name__ == '__main__':
    main()
