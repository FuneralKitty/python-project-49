import random

QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def progression():
    start = random.randint(1, 100)
    step = random.randint(2, 33)
    slice_step = random.randint(5, 10)
    pop_step = random.randint(1, 10)

    progression = list(range(start, 999, step))
    sliced_progression = progression[0:slice_step + 1]

    if pop_step > slice_step:
        pop_step = slice_step

    # we take this step out of progression
    operation = sliced_progression.pop(pop_step)
    sliced_progression.insert(pop_step, '..')
    quest = ' '.join(map(str, sliced_progression))

    return quest, operation
