import string

# Task 1

list_1 = list(range(1, 11, 1))

list_2 = list_1[5:]
list_1 = list_1[:5]

print(list_1)
print(f'{list_2}\n')

# Task 2

list_1.extend(list_2)
list_1.insert(0, 0)
list_3 = list_1.copy()
list_3.sort(reverse=True)

print(f'Original: {list_1}')
print(f'Copy: {list_3}\n')

# Task 3

text = input('Enter text: ')
uniq_characters = sorted(set(text.lower()))
print(f'{uniq_characters}\n')

# Task 4

months_pl = {
    1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec', 7: 'Lipiec',
    8: 'Sierpień', 9: 'Wrzesień', 10: 'Październik', 11: 'Listopad', 12: 'Grudzień'
}

print(f'{months_pl}\n')

# Task 5

moths_en = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

months = {'pl': months_pl, 'en': moths_en}

print(months['pl'][4])
print(f'{months['en'][4]}\n')

# Task 6

marianna = 'Marianna'

marianna_dict = dict.fromkeys(marianna, 1)
print(f'{marianna_dict}\n')

# Task 7

ascii_lowercase = set(string.ascii_lowercase)
digits = set(string.digits)
text_2 = set(input('Enter text: ').lower())

characters_match = text_2 & ascii_lowercase
digits_match = text_2 & digits

print(f'ASCII matches: {len(characters_match)} from {len(ascii_lowercase)} '
      f'({100 * len(characters_match) / len(ascii_lowercase):.2f}%)\n'
      f'Digits matches: {len(digits_match)} from {len(digits):.2f} '
      f'({100 * len(digits_match) / len(digits)}%)')
