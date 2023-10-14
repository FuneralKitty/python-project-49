#!/usr/bin/env python3
from brain_games.games.engine import start_game
from brain_games.games.brain_progression_logic import progression,description


def main():
    start_game(progression, description)


if __name__ == '__main__':
    main()
