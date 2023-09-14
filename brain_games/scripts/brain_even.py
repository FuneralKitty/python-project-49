# !/usr/bin/env python3
from brain_games.games.engine import start_game, even
from brain_games.games.brain_even_game import play_game 


def main():
    start_game(play_game,even)


if __name__ == '__main__':
    main()