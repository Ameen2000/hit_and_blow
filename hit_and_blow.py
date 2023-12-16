from itertools import permutations
import random
import hit_and_blow_algo_2

balls = ['R', 'B', 'G', 'P', 'Y', 'W']
combos = list(permutations(balls, 4)) # All possible permutations of 4 balls given 6 choices
winning_combo = random.choice(combos)
