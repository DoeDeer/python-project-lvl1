# -*- coding: utf-8 -*-

"""Module that provides cli methods."""

import prompt


def welcome_user(additional_text=None):
    """
    User greeting function.

    Args:
        additional_text: additional text, that would be printed after greeting

    Returns:
        Inputted user name

    """
    print('Welcome to the Brain Games!')
    if additional_text:
        print(additional_text)
    name = prompt.string('\nMay I have your name? ')
    print('Hello, {name}!\n'.format(name=name))
    return name
