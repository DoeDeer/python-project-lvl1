# -*- coding: utf-8 -*-

"""Brain games even game executable module."""

from brain_games import cli
from brain_games.games import engine, games


def main():
    """Start game."""
    name = cli.welcome_user(
        'Answer "yes" if number even otherwise answer "no".',
    )
    engine.core(name, games.even_game)


if __name__ == '__main__':
    main()
