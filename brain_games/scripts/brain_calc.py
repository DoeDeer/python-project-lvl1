# -*- coding: utf-8 -*-

"""Brain games calc game executable module."""

from brain_games import cli
from brain_games.games import engine, games


def main():
    """Start game."""
    name = cli.welcome_user('What is the result of the expression?')
    engine.core(name, games.calc_game)


if __name__ == '__main__':
    main()
