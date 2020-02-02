# -*- coding: utf-8 -*-

"""Games logic module."""

from random import randint

import prompt


def even_game(name):
    """Start an even game.

    Args:
        name: name of a player

    """
    for _try_num in range(0, 3):
        question = randint(1, 100)  # noqa: S311
        print('Question: {number}'.format(number=question))
        answer = prompt.string('Your answer: ')
        right_answer = 'yes' if not question % 2 else 'no'

        if answer == right_answer:
            print('Correct!')
        else:
            output_text = """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!"""
            output_text = output_text.format(answer, right_answer, name)
            print(output_text)
            break
    else:
        print('Congratulations, {name}!'.format(name=name))
