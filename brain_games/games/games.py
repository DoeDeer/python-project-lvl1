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
    question = random.randint(1, 100)
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
        'num1': random.randint(1, 100),
        'num2': random.randint(1, 100),
        'operator': random.choice(tuple(operators.keys())),
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
    question = (random.randint(1, 100), random.randint(1, 100))
    right_answer = math.gcd(question[0], question[1])
    return '{0} {1}'.format(*question), str(right_answer)


def progression_game():  # noqa: WPS210
    """Progression game logic.

    Returns:
        question and correct answer as string

    """
    progression_len = 10

    start_number = random.randint(1, 100)
    progression_step = random.randint(1, 20)  # noqa: WPS432
    progression = range(
        start_number,
        start_number + progression_step * progression_len,
        progression_step,
    )
    progression = list(map(str, progression))
    replaced_item_index = random.randint(0, len(progression) - 1)

    right_answer = progression[replaced_item_index]
    progression[replaced_item_index] = '..'

    return ' '.join(progression), right_answer


def prime_game():
    """Prime number game logic.

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
