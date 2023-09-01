#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    input_name = name
    return input_name
