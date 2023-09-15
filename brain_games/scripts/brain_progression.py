# !/usr/bin/env python3
from brain_games.games.engine import start_game, progress
from brain_games.games.brain_progression_logic import progression


def main():
    start_game(progression, progress)


if __name__ == '__main__':
    main()
