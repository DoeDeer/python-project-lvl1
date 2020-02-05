# -*- coding: utf-8 -*-

"""Progression game module."""

import random

DESCRIPTION = 'What number is missing in the progression?'


def run_round():  # noqa: WPS210
    """Check missing number in arithmetical progression.

    Returns:
        question and correct answer as string

    """
    PROGRESSION_LEN = 10  # noqa: N806

    start_number = random.randint(1, 100)
    progression_step = random.randint(1, 20)  # noqa: WPS432
    progression = range(
        start_number,
        start_number + progression_step * PROGRESSION_LEN,
        progression_step,
    )
    progression = list(map(str, progression))
    replaced_item_index = random.randint(0, len(progression) - 1)

    right_answer = progression[replaced_item_index]
    progression[replaced_item_index] = '..'

    return ' '.join(progression), right_answer
