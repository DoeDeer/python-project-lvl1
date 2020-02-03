# -*- coding: utf-8 -*-

"""Brain games gcd game executable module."""

from brain_games import cli
from brain_games.games import engine, games


def main():
    """Start game."""
    name = cli.welcome_user(
        'Find the greatest common divisor of given numbers.',
    )
    engine.core(name, games.gcd_game)


if __name__ == '__main__':
    main()
