# Task 1
import csv
from datetime import datetime
from typing import Any, Dict


def extract_numbers(vals: list[Any]) -> list[int | float]:
    return list(filter(lambda x: isinstance(x, (int, float)), vals))


things = ['A', 'Abc', 'utf-8', 8, ' ', 9.4]
print('Extracted numbers:', things, extract_numbers(things), sep='\n')

# Task 2

word_list = input('\nEnter words: ').split()
print('Your words: ', word_list)

sorted_words = sorted(word_list, key=lambda x: len(x), reverse=True)
print('Your sorted words: ', sorted_words)


# Task 3


def sort_ints_and_strs(vals: list[int | str], reversed=False) -> list[int | str]:
    if reversed:
        return sorted(vals, key=lambda x: (isinstance(x, int), x))
    else:
        return sorted(vals, key=lambda x: (isinstance(x, str), x))


ints_and_strs = ['bbb', 2, 1, 'aaa', 5, 'eee', 'ddd', 4, 'ccc', 3]

print('\n', ints_and_strs)
print(sort_ints_and_strs(ints_and_strs))
print(sort_ints_and_strs(ints_and_strs, reversed=True), '\n')


# Task 4


def save_to_csv(filename, rows):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter=';')
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def clean_row(row):
    row['Utarg'] = row['Utarg'].replace(' z', '').replace(',', '.').replace(' ', '')
    row['Data zamowienia'] = datetime.strptime(row['Data zamowienia'], "%d.%m.%Y").strftime('%Y-%m-%d')
    return row


with open('zamowienia.csv', newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    rows_poland = list(map(clean_row, filter(lambda row: row['Kraj'] == 'Polska', reader)))

with open('zamowienia.csv', newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    rows_germany = list(map(clean_row, filter(lambda row: row['Kraj'] == 'Niemcy', reader)))

save_to_csv('zamowienia_polska.csv', rows_poland)
save_to_csv('zamowienia_niemcy.csv', rows_germany)


# Task 5


def sort_dict_by_function(input_dict: Dict[str, list[int]], fun):
    """Examples of  functions:

    - min: ascending sort based on the smallest value

    - max: ascending sort based on the largest value

    - sum: ascending sort based on the sum of values

    - abs: ascending sort based on absolute value
    """
    if fun == abs:
        return dict(sorted(input_dict.items(), key=lambda item: max(map(abs, item[1]))))
    else:
        return dict(sorted(input_dict.items(), key=lambda item: fun(item[1])))


dictionary = {'Jan': [1, 2, 3, -6], 'Adam': [10, 20, -40]}
print(sort_dict_by_function(dictionary, min))
print(sort_dict_by_function(dictionary, max))
print(sort_dict_by_function(dictionary, sum))
print(sort_dict_by_function(dictionary, abs))
