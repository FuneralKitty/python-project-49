import random
from brain_games.games.constants import (progression_step_num,
                                         progression_end_step_num,
                                         progression_slice_step_num,
                                         progression_start_num)

description = 'What number is missing in the progression?'

import random
def progression(length=10, min_length=5):
    start = random.randint(1, 50)  # Adjust the range as needed
    step = random.randint(1, 10)  # Adjust the range as needed
    end = start + (length - 1) * step
    hidden_index = random.randint(0, length - 1)
    progression = list(range(start, end + step, step))
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    progression_str = ' '.join(map(str, progression))
    return progression_str, hidden_value
