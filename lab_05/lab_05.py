import math
import random

from typing import List, Tuple

# Task 1

A = {1 / x for x in range(1, 11)}
B = {2 ** x for x in range(0, 11)}
C = {x for x in B if x % 4 == 0}

print(A, B, C,  sep='\n')

# Task 2

dim = 4  # 4x4
matrix = [[random.randint(1, 1000) for _ in range(dim)] for _ in range(dim)]
diagonal = [matrix[i][i] for i in range(dim)]

print('\n', matrix, diagonal, sep='\n')

# Task 3

text = 'Ala ma kota.'
text_generator = ((word, [ord(char) for char in word]) for word in text.split())

print('\n', list(text_generator))

# Task 4


def quadratic_equation_solver(a: int | float, b: int | float, c: int | float) \
        -> int | float | tuple[int | float, int | float] | None:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return None
    elif delta == 0:
        x = (-b) / (2 * a)
        return x
    else:
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

# Task 5


def throw_the_dice_n(n: int) -> List[Tuple[str, str]]:
    results = (random.randint(1, 6) for _ in range(n))

    dictionary_of_results = {}
    for result in results:
        dictionary_of_results[result] = dictionary_of_results.get(result, 0) + 1

    returned_list = []
    for key, value in sorted(dictionary_of_results.items(), key=lambda item: item[0]):
        returned_list.append((f'number: {key}', f'rolls: {value}'))

    return returned_list


while True:
    num = input('\nEnter your integer: ')

    if num.isdigit():
        num = int(num)
        break
    else:
        print('Enter a valid integer.')

print(throw_the_dice_n(num))

# Task 6


def sort_strings(*texts: str) -> List[str]:
    return sorted(texts)


print('\n', sort_strings('Cipher', 'Adam', 'Drax', 'Bart'))

# Task 7


def sum_of_scores(**teams_scores: int) -> int:
    return sum(teams_scores.values())


print('\n', sum_of_scores(delta_1=3, real_atletico=19, bavarians=11, polandos=7))
