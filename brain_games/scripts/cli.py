# -*- coding: utf-8 -*-

"""Module that provides cli methods."""

import prompt


def welcome_user():
    """Say hello, be friendly."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
