# -*- coding: utf-8 -*-

"""Brain games progression game executable module."""

from brain_games import cli
from brain_games.games import engine, games


def main():
    """Start game."""
    name = cli.welcome_user(
        'What number is missing in the progression?',
    )
    engine.core(name, games.progression_game)


if __name__ == '__main__':
    main()
