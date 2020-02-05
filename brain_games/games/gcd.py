# -*- coding: utf-8 -*-

"""GCD game module."""

import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def run_round():
    """Check numbers GCD.

    Returns:
        question and correct answer as string

    """
    question = (random.randint(1, 100), random.randint(1, 100))
    right_answer = math.gcd(question[0], question[1])
    return '{0} {1}'.format(*question), str(right_answer)
