# -*- coding: utf-8 -*-

"""Games core functions."""

import prompt

from brain_games import cli

WRONG_ANSWER_TEMPLATE = """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!"""


def run(game):
    """Start an provided game.

    Args:
        game: game module, that includes game greeting and run function

    """
    name = cli.welcome_user(game.DESCRIPTION)

    for _try_num in range(0, 3):
        question, right_answer = game.run_round()
        print('Question: {question}'.format(question=question))
        user_answer = prompt.string('Your answer: ')

        if user_answer != right_answer:
            print(WRONG_ANSWER_TEMPLATE.format(user_answer, right_answer, name))
            break
        print('Correct!')
    else:
        print('Congratulations, {name}!'.format(name=name))
