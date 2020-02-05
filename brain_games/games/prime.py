# -*- coding: utf-8 -*-

"""Prime game module."""

import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_round():
    """Check number prime.

    Returns:
        question and correct answer as string

    """
    question = random.randint(1, 100)
    is_prime = True
    division_check_till = int(question ** 0.5) + 1
    for num in range(2, division_check_till):
        if not question % num:  # noqa: S001
            is_prime = False
            break
    right_answer = 'yes' if is_prime else 'no'
    return str(question), right_answer
