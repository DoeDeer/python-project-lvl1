#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Brain games prime number game executable module."""

from brain_games import cli
from brain_games.games import engine, games


def main():
    """Start game."""
    name = cli.welcome_user(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
    )
    engine.core(name, games.prime_game)


if __name__ == '__main__':
    main()
