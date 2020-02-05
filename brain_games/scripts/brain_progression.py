#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Brain games progression game executable module."""

from brain_games import engine, games


def main():
    """Start game."""
    engine.run(games.progression)


if __name__ == '__main__':
    main()
