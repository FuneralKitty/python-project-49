#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import play_game

def main():
    print("Welcome to the Brain Games!")

welcome_user()
play_game()

if __name__ == '__main__':
    main()
    welcome_user()
    play_game()