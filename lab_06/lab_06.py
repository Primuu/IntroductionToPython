import csv
import random
from datetime import datetime
from typing import List
from unidecode import unidecode


# Task 1


def save_to_csv(filename, rows):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter=';')
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


rows_poland = []
rows_germany = []

with open('zamowienia.csv', newline='', errors='ignore') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        # print(row['Data zamowienia'], ' - ', row['Utarg'])

        row['Utarg'] = row['Utarg'].replace(' z', '').replace(',', '.').replace(' ', '')
        row['Data zamowienia'] = datetime.strptime(row['Data zamowienia'], "%d.%m.%Y").strftime('%Y-%m-%d')

        # print(row['Data zamowienia'], ' - ', row['Utarg'])

        if row['Kraj'] == 'Polska':
            rows_poland.append(row)
        elif row['Kraj'] == 'Niemcy':
            rows_germany.append(row)

save_to_csv('zamowienia_polska.csv', rows_poland)
save_to_csv('zamowienia_niemcy.csv', rows_germany)


# Task 2


def merge_files(file_list: List[str], file_name: str) -> None:
    try:
        with open(file_name, 'w') as file_writer:
            for name in file_list:
                with open(name, 'r') as file_reader:
                    file_writer.write(file_reader.read())
    except OSError as err:
        print(f'Error: {err}')


merge_files(['zamowienia_polska.csv', 'zamowienia_niemcy.csv'], 'zamowienia_pl_ger.csv')

# Task 3


def n_extremes(numeric_list, n, minimal=True):
    if not all(isinstance(num, (int, float)) for num in numeric_list):
        raise ValueError("List contains other values than numbers.")
    if minimal:
        return sorted(numeric_list)[:n]
    else:
        return sorted(numeric_list, reverse=True)[:n]


print(n_extremes([5, 7, 3, 4, 2, 6, 9, 1, 8, 10], 3, minimal=True))
print(n_extremes([5, 7, 3, 4, 2, 6, 9, 1, 8, 10], 3, minimal=False))
# print(n_extremes([5, 'a', 3, 4, 2, 6, 9, 1, 8, 10], 3))

# Task 4

mixed = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]


def to_dict_by_type(mixed_list):
    result = {}
    for item in mixed_list:
        type_name = type(item).__name__
        if type_name not in result:
            result[type_name] = []
        result[type_name].append(item)
    return result


print('\n', to_dict_by_type(mixed))

# Task 5


def save_last_names(last_names: List[str]) -> None:
    with (open('A-M_nazwiska.txt', 'w', encoding='utf-8') as a_m_last_names,
          open('N-Ż_nazwiska.txt', 'w', encoding='utf-8') as n_z_last_names):
        for last_name in last_names:
            normalized_last_name = unidecode(last_name).upper()
            if 'A' <= normalized_last_name[0] <= 'M':
                a_m_last_names.write(last_name + '\n')
            elif 'N' <= normalized_last_name[0] <= 'Z':
                n_z_last_names.write(last_name + '\n')


last_names = ['Kowalski', 'Nowak', 'Wiśniewski', 'Dąbrowski', 'Lewandowski', 'Wójcik', 'Kamiński',
              'Kaczmarek', 'Zawisza', 'Ślusarczyk', 'Skowyrski', 'Żubrowicz']
save_last_names(last_names)

# Task 6


def reverse_words(text: str) -> None:
    split_text = text.split(' ')
    reversed_text = ' '.join(word[::-1] for word in split_text)
    print(reversed_text)


print()
reverse_words('Ala ma kota')

# Task 7


def deal_cards(players: List[str], card_number: int) -> None:
    colors = ['pik', 'kier', 'karo', 'trefl']
    figures = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Walet', 'Dama', 'Król', 'As']
    deck = [f'{figure} {color}' for color in colors for figure in figures]
    random.shuffle(deck)

    players_cards = {player: [] for player in players}

    for i in range(card_number):
        for player in players:
            players_cards[player].append(deck.pop())

    for player, card in players_cards.items():
        print(f'{player}: {card}')


print()
deal_cards(['Adam', 'Tom', 'Ned', 'Bazyl', 'Piter123'], 5)

# Task 8

people = ['Marek Markowski', 'Paweł Budzikowski', 'Mirosław Wójcik', 'Janusz Kowalski', 'Tom Malinowski', 'Ned Stark']


def save_to_file(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file_writer:
        for i, item in enumerate(data):
            if i > 0:
                file_writer.write('\n')
            file_writer.write(item)


def to_email_save(file: str, domain: str, output_file: str) -> None:
    with (open(file, 'r', encoding='utf-8', errors='ignore') as file_reader,
          open(output_file, 'w', encoding='utf-8') as file_writer):
        for line in file_reader:
            line = line.strip()
            name, last_name = line.split()
            name, last_name = unidecode(name).lower(), unidecode(last_name).lower()
            email = f'{name}.{last_name}@{domain}'

            file_writer.write(f'{line}, {email}\n')


save_to_file('people.txt', people)
to_email_save('people.txt', 'student.uwm.edu.pl', 'emails.txt')

# Task 9

sentences = ['Hello World', 'Bez pracy nie ma kołaczy', 'Cieśnina Gibraltarska']
save_to_file('sentences.txt', sentences)


def wheel_of_fortune(sentences: str):
    sentences_read = []
    with open(sentences, 'r', encoding='utf-8') as file_reader:
        for line in file_reader:
            sentences_read.append(line.strip())

    password = random.choice(sentences_read)
    password_l = password.lower()
    hidden_password = ['_' if char != ' ' else ' ' for char in password]
    print('Guess password:', ' '.join(hidden_password))

    while True:
        guess = input('Guess a letter or a whole password: ').strip().lower()

        if len(guess) == 1:
            if guess in password_l:
                print('This letter is in password!')
                hidden_password = [password[i] if password_l[i] == guess else hidden_password[i]
                                   for i in range(len(password))]
            else:
                print('This letter is not in password!')

            if '_' not in hidden_password:
                print('Congratulations! You guessed the password!')
                print(password)
            else:
                print('\nGuess password:', ' '.join(hidden_password))
        else:
            if guess == password_l:
                print('Congratulations! You guessed the password!')
                print(password)
                break
            else:
                print('Wrong! Try again!')


print()
wheel_of_fortune('sentences.txt')
