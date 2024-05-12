import datetime
import random
import time
from array import array
from collections import deque, namedtuple, Counter
from timeit import timeit

import numpy as np

# Task 1

setup = """
from array import array
import random
"""

stmt_char_array = "char_array = array('u', [chr(random.randint(0, 127)) for _ in range(1_000_000)])"
stmt_char_list = "char_list = [chr(random.randint(0, 127)) for _ in range(1_000_000)]"

stmt_int_array = "int_array = array('i', [random.randint(0, 1000) for _ in range(1_000_000)])"
stmt_int_list = "int_list = [random.randint(0, 1000) for _ in range(1_000_000)]"

stmt_long_array = "long_array = array('l', [random.randint(0, 1000) for _ in range(1_000_000)])"
stmt_long_list = "long_list = [random.randint(0, 1000) for _ in range(1_000_000)]"

print("Character array initialization time:", timeit(stmt_char_array, setup, number=10))
print("Character list initialization time:", timeit(stmt_char_list, setup, number=10))

print("Integer array initialization time:", timeit(stmt_int_array, setup, number=10))
print("Integer list initialization time:", timeit(stmt_int_list, setup, number=10))

print("Long array initialization time:", timeit(stmt_long_array, setup, number=10))
print("Long list initialization time:", timeit(stmt_long_list, setup, number=10))

# Task 2

# array

tab_of_floats = array('f', [random.random() for _ in range(1_000_000)])

start_time = datetime.datetime.now()

with open('floats_array.bin', 'wb') as file_arr:
    tab_of_floats.tofile(file_arr)

end_time = datetime.datetime.now()
print(f'\nArray write time: {end_time - start_time}')

start_time = datetime.datetime.now()

tab_of_floats_loaded = array('f')
file_arr = open('floats_array.bin', 'rb')
tab_of_floats_loaded.fromfile(file_arr, 1_000_000)
file_arr.close()

end_time = datetime.datetime.now()
print(f'Array read time: {end_time - start_time}')

# list

start_time = datetime.datetime.now()

list_of_floats = [random.random() for _ in range(1_000_000)]
with open('floats_list.txt', 'w') as file_arr:
    file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))

end_time = datetime.datetime.now()
print(f'List write time: {end_time - start_time}')

start_time = datetime.datetime.now()

with open('floats_list.txt', 'r') as file_list:
    list_of_floats_loaded = file_list.readlines()

list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]

end_time = datetime.datetime.now()
print(f'List read time: {end_time - start_time}')

# Task 3

setup_deque = "from collections import deque; d = deque()"
setup_list = "l = []"

print(f'\nDeque append: {timeit("d.append(0)", setup=setup_deque, number=100_000)}')
print(f'Deque append left: {timeit("d.appendleft(0)", setup=setup_deque, number=100_000)}')
print(f'List append: {timeit("l.append(0)", setup=setup_list, number=100_000)}')
print(f'List insert(0): {timeit("l.insert(0, 0)", setup=setup_list, number=100_000)}')

# Task 4

with open('zamowienia.csv', 'r', newline='\n', errors='ignore') as csvfile:
    headers = csvfile.readline().strip().split(';')
    headers = [header.replace(' ', '_') for header in headers]

    Order = namedtuple('Order', headers)

    print()

    for i, record in enumerate(csvfile):
        order = Order._make(record.strip().split(';'))
        print(order)
        if i > 10:
            break


# Task 5


def top_ten_percent(nums):
    n = len(nums)
    if n == 0:
        return None
    else:
        n = max(1, int(0.1 * n))
        nums_sorted = sorted(nums, reverse=True)
        return nums_sorted[:n]


print('\n', top_ten_percent(array('I', [i for i in range(1, 16)])))
print(top_ten_percent(array('I', [])))


# Task 6


def create_kolo_fortuny(*args):
    counter = Counter(args)

    result_deque = deque()
    for item, count in counter.items():
        result_deque.extend([item] * count)

    return result_deque


result = create_kolo_fortuny('banan', 'koza', 'banan', 'z nosa', 'koza', 'piesek', 'banan', 'lama', 'banan', )
print('\n', result)


# Task 7


def spin_it(deque_object, ticks: int):
    waits = np.logspace(0.0, 1.0, num=ticks) / ticks

    for tick in range(ticks):
        print(f'{deque_object[0]}', end='')
        time.sleep(waits[tick])
        print('\r', end='')
        deque_object.rotate(-1)

    print(f'Wheel stopped at: {deque_object[0]}')


wheel_1 = create_kolo_fortuny('apple', 'banana', 'apple', 'orange', 'banana', 'banana')
wheel_2 = create_kolo_fortuny('wolf', 'lion', 'monkey', 'cow', 'sloth', 'donkey')
wheel_3 = create_kolo_fortuny('100 $', '200 $', '1 $', '1000 $', '5000 $', '2 $', '0 $', '1 000 000 $')

spin_it(wheel_1, 200)
spin_it(wheel_2, 200)
spin_it(wheel_3, 200)
