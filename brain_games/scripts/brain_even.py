#!/usr/bin/env python3
from brain_games.scripts.brain_games import main
from brain_games.engines.brain_even_game import play_game
from brain_games.engines.cli import welcome_user

if __name__ == '__main__':
    main()
    welcome_user()
    play_game()