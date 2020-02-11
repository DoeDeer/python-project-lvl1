# -*- coding: utf-8 -*-

"""Even game module."""

import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    """Predicate function, check given number even.

    Args:
        number: number to check

    Returns:
        even of the number

    """
    return not number % 2


def run_round():
    """Check random number for even.

    Returns:
        question and correct answer as string

    """
    question = random.randint(1, 100)
    right_answer = 'yes' if is_even(question) else 'no'
    return str(question), right_answer
