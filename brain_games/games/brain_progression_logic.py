import random


description = 'What number is missing in the progression?'


def progression():
    progression_start = random.randint(1, 100)
    progression_step = random.randint(2, 33)
    progression_slice_step = random.randint(5, 10)
    progression_end_step = random.randint(101, 999)

    progression = list(range(progression_start, progression_end_step, progression_step))
    sliced_progression = progression[0:progression_slice_step + 1]

    if pop_step > progression_slice_step:
        pop_step = progression_slice_step

    # we take this step out of progression
    operation = sliced_progression.pop(pop_step)
    sliced_progression.insert(pop_step, '..')
    quest = ' '.join(map(str, sliced_progression))

    return quest, str(operation)
