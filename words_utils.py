import json


def add_new_word(word):
    with open('words.json') as file:
        words = json.load(file)

    if word not in words:
        words.append(word.lower())
        with open('words.json', 'w') as file:
            json.dump(words, file)

        print(f'Слово {word.upper()} добавлено')

    else:
        print(f'Слово {word.upper()} уже есть в списке')

