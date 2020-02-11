# -*- coding: utf-8 -*-

"""Prime game module."""

import math
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(number):
    """Predicate function, check given number prime.

    Args:
        number: number to check

    Returns:
        prime of the number

    """
    division_check_till = int(math.sqrt(number)) + 1
    for num in range(2, division_check_till):
        if not number % num:  # noqa: S001 , that's bug of linter
            return False
    return True


def run_round():
    """Check number prime.

    Returns:
        question and correct answer as string

    """
    question = random.randint(1, 100)
    right_answer = 'yes' if check_prime(question) else 'no'
    return str(question), right_answer
