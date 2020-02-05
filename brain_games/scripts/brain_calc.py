#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Brain games calc game executable module."""

from brain_games import engine, games


def main():
    """Start game."""
    engine.run(games.calc)


if __name__ == '__main__':
    main()
