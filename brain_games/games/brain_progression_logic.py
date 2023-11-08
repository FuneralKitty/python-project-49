import random
from brain_games.games.constants import (progression_step_num,
                                         progression_end_step_num,
                                         progression_slice_step_num,
                                         progression_start_num)

description = 'What number is missing in the progression?'

#progression_
def progression():
    progression_start = random.randint(*progression_start_num)
    progression_step = random.randint(*progression_step_num)
    progression_slice_step = random.randint(*progression_slice_step_num)
    progression_end_step = random.randint(*progression_end_step_num)

    progression = list(range(progression_start, progression_end_step, progression_step))
    sliced_progression = progression[0:progression_slice_step + 1]

    if progression_end_step > progression_slice_step:
        progression_end_step = progression_slice_step

    # we take this step out of progression
    operation = sliced_progression.pop(progression_end_step)
    sliced_progression.insert(progression_end_step, '..')
    quest = ' '.join(map(str, sliced_progression))

    return quest, str(operation)
