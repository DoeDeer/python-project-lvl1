# -*- coding: utf-8 -*-

"""Calc game module."""

import operator
import random

DESCRIPTION = 'What is the result of the expression?'

OPERATORS = (
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
)


def run_round():
    """Check simple equation.

    Returns:
        question and correct answer as string

    """
    symbol, operation = random.choice(OPERATORS)
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    right_answer = operation(num1, num2)
    return '{0} {1} {2}'.format(num1, symbol, num2), str(right_answer)
