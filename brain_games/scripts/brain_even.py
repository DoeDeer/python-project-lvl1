#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Brain games even game executable module."""

from brain_games import engine, games


def main():
    """Start game."""
    engine.run(games.even)


if __name__ == '__main__':
    main()
