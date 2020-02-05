# -*- coding: utf-8 -*-

"""Even game module."""

import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def run_round():
    """Check random number for even.

    Returns:
        question and correct answer as string

    """
    question = random.randint(1, 100)
    right_answer = 'yes' if not question % 2 else 'no'
    return str(question), right_answer
