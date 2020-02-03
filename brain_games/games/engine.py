# -*- coding: utf-8 -*-

"""Games core functions."""

import prompt


def core(name, logic_function):
    """Start an provided game.

    Args:
        name: name of a player,
        logic_function: function, that returns question and correct answer.

    """
    for _try_num in range(0, 3):
        question, right_answer = logic_function()
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
