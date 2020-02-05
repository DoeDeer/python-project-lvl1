# -*- coding: utf-8 -*-

"""Calc game module."""

import operator
import random

DESCRIPTION = 'What is the result of the expression?'


def run_round():
    """Check simple equation.

    Returns:
        question and correct answer as string

    """
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    question = {
        'num1': random.randint(1, 100),
        'num2': random.randint(1, 100),
        'operator': random.choice(tuple(operators.keys())),
    }
    right_answer = operators[question['operator']](
        question['num1'],
        question['num2'],
    )
    return '{num1} {operator} {num2}'.format(**question), str(right_answer)
