# Task 1
int_1 = int('101', base=2)
int_2 = int('A1', 16)

print(f'Integer 1: {int_1}')
print(f'Integer 2: {int_2}\n')

float_1 = float(7)
float_2 = float('3.1415')

print(f'Float 1: {float_1}')
print(f'Float 2: {float_2}\n')

# Task 2

x = 21  # binary 10101
x_bit_counter = x.bit_count()
print(f'x bit counter: {x_bit_counter}\n')

float_3 = 3.1415
float_4 = 4.0

is_integer = float_3.is_integer()
print(f'float_3 is integer: {is_integer}')

is_integer = float_4.is_integer()
print(f'float_4 is integer: {is_integer}\n')

# Task 3

number = 123
binary_number = bin(number)
print(f'Binary representation of {number}: {binary_number}')

number_from_binary = int(binary_number, 2)
print(f'Decimal representation of {binary_number}: {number_from_binary}\n')

# Task 4

int_3 = int('11010', base=2)
int_4 = int('10101', base=2)

n = 3

logic_or_example = int_3 | int_4
logic_and_example = int_3 & int_4
logic_xor_example = int_3 ^ int_4
left_bitshift = int_3 << n

multiplying = int_3 * 2 ** n

print(f'Logical or example: {bin(int_3)} | {bin(int_4)} = {bin(logic_or_example)}')
print(f'Logical and example: {bin(int_3)} & {bin(int_4)} = {bin(logic_and_example)}')
print(f'Logical xor example: {bin(int_3)} ^ {bin(int_4)} = {bin(logic_xor_example)}')
print(f'Shift {int_3} by {n} bits left is {left_bitshift},'
      f' and it\'s equal to multiply {int_3} * 2^{n} ({multiplying})\n')

# Task 5

float_5 = 16.2
float_5_hex = float_5.hex()
number_from_hex = float.fromhex(float_5_hex)

print(f'Hex representation of {float_5}: {float_5_hex}')
print(f'Decimal representation of {float_5_hex}: {number_from_hex}')
