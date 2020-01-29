# -*- coding: utf-8 -*-

"""Brain games main executable module."""

from brain_games import cli


def main():
    """Start game."""
    print('Welcome to the Brain Games!\n')  # noqa: T001
    cli.welcome_user()


if __name__ == '__main__':
    main()
