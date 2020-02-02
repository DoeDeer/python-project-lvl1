# -*- coding: utf-8 -*-

"""Brain games even game executable module."""

from brain_games import cli, games


def main():
    """Start game."""
    print(
        'Welcome to the Brain Games!\n',
        'Answer "yes" if number even otherwise answer "no".\n',
        sep='',
    )
    name = cli.welcome_user()
    games.even_game(name)


if __name__ == '__main__':
    main()
