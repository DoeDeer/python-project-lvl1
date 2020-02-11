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
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    right_answer = math.gcd(num1, num2)
    return '{0} {1}'.format(num1, num2), str(right_answer)
