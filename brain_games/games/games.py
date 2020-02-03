# -*- coding: utf-8 -*-

"""Games  logic functions."""

import math
import operator
import random


def even_game():
    """Even game logic.

    Returns:
        question and correct answer as string

    """
    question = random.randint(1, 100)  # noqa: S311
    right_answer = 'yes' if not question % 2 else 'no'
    return str(question), right_answer


def calc_game():
    """Calc game logic.

    Returns:
        question and correct answer as string

    """
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    question = {
        'num1': random.randint(1, 100),  # noqa: S311
        'num2': random.randint(1, 100),  # noqa: S311
        'operator': random.choice(tuple(operators.keys())),  # noqa: S311
    }
    right_answer = operators[question['operator']](
        question['num1'],
        question['num2'],
    )
    return '{num1} {operator} {num2}'.format(**question), str(right_answer)


def gcd_game():
    """GCD game logic.

    Returns:
        question and correct answer as string

    """
    question = (random.randint(1, 100), random.randint(1, 100))  # noqa: S311
    right_answer = math.gcd(question[0], question[1])
    return '{0} {1}'.format(*question), str(right_answer)
