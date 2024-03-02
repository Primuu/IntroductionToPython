# Task 1

data_line = input('Enter data line separated by any separator (space, semicolon, etc.): ')
source_separator = input('Enter source separator: ')
target_separator = input('Enter target separator: ')

data_line_split = data_line.split(source_separator)
result = target_separator.join(data_line_split)

print(f'Processed data:\n{result}\n')

# Task 2

data_line_2 = input('Enter data line: ')
half_of_length = len(data_line_2) // 2  # integer division
slice_1 = data_line_2[:half_of_length]
slice_2 = data_line_2[half_of_length:]

print(f'Data line separated:\n1. {slice_1}\n2. {slice_2}')
print(f'Every second character from the of the data line: {data_line_2[::-2]}\n')

# Task 3

data_line_3 = 'Shut up and calculate ~ Richard Feynman'
print(data_line_3)
print(f'\nLooks like title now: {data_line_3.title()}')
print(f'Capitalized only 1st letter:{data_line_3.capitalize()}')
print(f'Filled with zeros to length = 50: {data_line_3.zfill(50)}')
print(f'Every character uppercase: {data_line_3.upper()}')
print(f'Number of occurrences of \'u\' in the sentence: {data_line_3.count('u')}')
print(f'Centered sentence (70 characters):\n{data_line_3.center(70)}\n')

# Task 4

data_line_4 = input('Enter data line: ')

print(f'Does the data line consist only of letters? - {data_line_4.isalpha()}')
print(f'Are all characters in the data line ascii characters? - {data_line_4.isascii()}')
print(f'Are all characters in the data line printable? - {data_line_4.isprintable()}')
print(f'Is the data line in title format? - {data_line_4.istitle()}')
print(f'Does the data line consist only of capital letters? - {data_line_4.isupper()}\n')

# Task 5

text = 'Damn beaver'
number = 3.14159265

print(f'Right alignment:\n{text:>20}')
print(f'Left alignment with padding:\n{text:_>20}')
print(f'Centering:\n{text:^20}')
print(f'Formatting number ({number}) = {number:.2f}')
print(f'Adding a plus sign for positive float: {number:+f}\n')

# Task 6

print('1. \u0B27')
print('2. \uFF21')
print('3. \u1001')
print('4. \uFE3B')
print('5. \uFE19')
print('6. \u1014')
print('7. \uBC12')
print('8. \u01AC')
print('9. \uA12C')
print('10. \u3B12')
