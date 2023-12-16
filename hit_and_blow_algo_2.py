import random
from itertools import permutations

balls = ['R', 'G', 'B', 'P', 'Y', 'W']





def score_function(winning_combo, comp_guess):
    right_position = 0
    right_colour = 0
    j = 0
    for colour in comp_guess:
        if colour in winning_combo and colour == winning_combo[j]:
            right_position += 1
            j += 1
        elif colour in winning_combo and colour != winning_combo[j]:
            right_colour += 1
            j += 1
        else:
            j += 1
    score = (right_position, right_colour)

    return score


def hit_and_blow_solver():
    combos = list(permutations(balls, 4))
    winning_combo = random.choice(combos)
    comp_guess = random.choice(combos)
    possibilities = combos
    tries = 1
    if comp_guess == winning_combo:
        print(comp_guess)
        print("Solved!")
        print("Wow first try!")
    while comp_guess != winning_combo:
        possibilities.remove(comp_guess)
        score = score_function(winning_combo, comp_guess)
        j = 0
        for _ in range(len(possibilities)):
            if score_function(possibilities[j], comp_guess) != score:
                possibilities.pop(j)
            else:
                j += 1
        number_of_possibilities = str(len(possibilities))
        guess = str(comp_guess)
        print(f"{guess} {number_of_possibilities}")

        comp_guess = random.choice(possibilities)
        tries += 1
    if tries > 1:
        final_guess = str(comp_guess)
        solution = str(winning_combo)
        number_of_tries = str(tries)
        print(f"The last guess is: {final_guess}.")
        print(f"The hidden code is: {solution}.")
        print(f"Took you {number_of_tries} tries.")
    return tries


def hit_and_blow_solver_f():
    combos = list(permutations(balls, 4))
    winning_combo = random.choice(combos)
    comp_guess = random.choice(combos)
    possibilities = combos
    tries = 1
    if comp_guess == winning_combo:
        print(comp_guess)
        print("Solved!")
        print("Wow first try!")
    while comp_guess != winning_combo:
        score = score_function(winning_combo, comp_guess)
        f = lambda x: True if (score_function(x, comp_guess) == score) else False
        possibilities = list(filter(f, possibilities))
        number_of_possibilities = str(len(possibilities))
        guess = str(comp_guess)
        print(f"{guess} {number_of_possibilities}")
        comp_guess = random.choice(possibilities)
        tries += 1
    if tries > 1:
        final_guess = str(comp_guess)
        solution = str(winning_combo)
        number_of_tries = str(tries)
        print(f"The last guess is: {final_guess}.")
        print(f"The hidden code is: {solution}.")
        print(f"Took you {number_of_tries} tries.")
    return tries


if __name__ == "__main__":
    tries = []
    for _ in range(10**4):
        tries.append(hit_and_blow_solver_f())
    print(tries)
    s = sum(tries)
    l = len(tries)
    print(s / l)
    print(max(tries))
