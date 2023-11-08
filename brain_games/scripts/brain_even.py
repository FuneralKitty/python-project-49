#!/usr/bin/env python3
from brain_games.games.engine import start_game
from brain_games.games.brain_even_game import play_game, description


def main():
    start_game(play_game, description)


if __name__ == '__main__':
    main()
