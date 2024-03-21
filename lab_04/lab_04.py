import random
import sys
import this

# Task 1

for i in range(51):
    if i % 5 == 0:
        print(i)

# Task 2

while True:
    height = input('\nEnter your height <3, 5, 7, 9>: ')

    if height.isdigit():
        height = int(height)

        if 3 <= height <= 9 and height % 2 != 0:
            break
        else:
            print('Enter an odd value between 3 and 9.')
    else:
        print('Enter a valid integer.')

middle = height // 2

for i in range(height):
    if i <= middle:
        line = ' ' * (middle - i)
        line += 'o' * (i * 2 + 1)
    else:
        line = ' ' * (i - middle)
        line += 'o' * ((height - i) * 2 - 1)
    print(line)

# Task 3

header = ' ' * 4
for i in range(1, 11):
    header += f'{i:>4}'
print('\n' + header)

for row in range(1, 11):
    row_data = f'{row:>3} '
    for col in range(1, 11):
        row_data += f'{row * col:>4}'
    print(row_data)

# Task 4

while True:
    num = input('\nEnter your integer: ')

    if num.isdigit():
        num = int(num)
        break
    else:
        print('Enter a valid integer.')

print(f'Bin: {bin(num)}')
print(f'Oct: {oct(num)}')
print(f'Hex: {hex(num)}')

# Task 5

i = input('\nEnter your number: ')

try:
    int_val = int(i)
    print('Your number is an integer.')
except ValueError:
    try:
        float_val = float(i)
        print('Your number is a float.')
    except ValueError:
        print('Your number is neither an integer nor a float.')

# Task 6

sys.stdout.write('\nEnter your integer: ')

while True:
    number = sys.stdin.readline().strip()

    if number.isdigit():
        break
    else:
        sys.stdout.write('Enter a valid integer: ')

line = '\nThe given number can be written as: '

length = len(number)
line += ' + '.join(f'{10 ** (length - i - 1)} * {digit}' for i, digit in enumerate(number))

sys.stdout.write(line)

# Task 7

coding = this.d
text_to_encode = input('\n\nEnter your sentence: ')

encoded_text = ''.join(coding.get(char, char) for char in text_to_encode)

print('Encoded sentence:', encoded_text)

# Task 8

sentence = input('\nEnter your sentence: ')

word_list = sentence.split()
sorted_word_list = sorted(word_list, key=len)

print('Sorted words:', ' '.join(sorted_word_list))

# Task 9

phrases = {
    '1': ['Koleżanki i koledzy', 'Z drugiej strony', 'Podobnie', 'Nie zapominajmy jednak, że', 'W ten oto sposób',
          'Praktyka dnia codziennego dowodzi, że',
          'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ',
          'Różnorakie i bogate doświadczenia', 'Troska organizacji, a szczególnie', 'Wyższe założenia ideowe, a także'],
    '2': ['realizacja nakreślonych zadań programowych', 'zakres i miejsce szkolenia kadr',
          'stały wzrost ilości i zakres naszej aktywności', 'aktualna struktura organizacji',
          'nowy model działalności organizacyjnej', 'dalszy rozwój różnych form działalności',
          'stałe zabezpieczenie informacyjno programowe naszej działalności', 'wzmacnianie i rozwijanie struktur',
          'konsultacja z szerokim aktywem', 'rozpoczęcie powszechnej akcji kształtowania postaw'],
    '3': ['zmusza nas do przeanalizowania', 'spełnia istotną rolę w kształtowaniu', 'wymaga sprecyzowania i określenia',
          'pomaga w przygotowaniu i realizacji', 'zabezpiecza udział szerokiej grupie w kształtowaniu',
          'spełnia ważne zadania w wypracowaniu', 'umożliwia w większym stopniu tworzenie', 'powoduje docenianie wagi',
          'przedstawia interesującą próbę sprawdzenia', 'pociąga za sobą proces wdrażania i unowocześniania'],
    '4': ['istniejących warunków administracyjno-finansowych.', 'dalszych kierunków rozwoju.',
          'systemu powszechnego uczestnictwa.', 'postaw uczestników wobec zadań stawianych przez organizację.',
          'nowych propozycji.', 'kierunków postępowego wychowania.',
          'systemu szkolenia kadry odpowiadającego potrzebom.', 'odpowiednich warunków aktywizacji.', 'modelu rozwoju.',
          'form oddziaływania.']
}

while True:
    n = input('\nEnter the number of sentences: ')

    if n.isdigit():
        n = int(n)
        break
    else:
        print('Enter a valid integer.')

for _ in range(n):
    sentence = ' '.join([random.choice(phrases[key]) for key in phrases])
    print(sentence)
