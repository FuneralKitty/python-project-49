#!/usr/bin/env python3
from brain_games import prompt

def welcome_user():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
