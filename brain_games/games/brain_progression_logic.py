import random
from brain_games.games.constants import progression_start,progression_step



description = 'What number is missing in the progression?'

import random
def progression(length=10, min_length=5):
    start = random.randint(*progression_start)  # Adjust the range as needed
    step = random.randint(*progression_step)  # Adjust the range as needed
    end = start + (length - 1) * step
    hidden_index = random.randint(0, length - 1)
    progression = list(range(start, end + step, step))
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    progression_str = ' '.join(map(str, progression))
    return progression_str, str(hidden_value)
