# -*- coding: utf-8 -*-

"""Games core functions."""

import prompt

from brain_games import cli


def run(game):  # noqa: WPS210
    """Start an provided game.

    Args:
        game: game module, that includes game greeting and run function

    """
    name = cli.welcome_user(game.DESCRIPTION)

    for _try_num in range(0, 3):
        question, right_answer = game.run_round()
        print('Question: {question}'.format(question=question))
        user_answer = prompt.string('Your answer: ')

        if user_answer == right_answer:
            print('Correct!')
        else:
            output_text = """'{0}' is wrong answer ;(. Correct answer was '{1}'.
Let's try again, {2}!"""
            output_text = output_text.format(user_answer, right_answer, name)
            print(output_text)
            break
    else:
        print('Congratulations, {name}!'.format(name=name))
