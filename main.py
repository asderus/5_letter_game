from utils import *

print_rules()

word = get_word()
words_data = get_words_data()
print('\nСлово загадано!')
is_guess = False
user_try = 1

while user_try <= 5:
    user_word = input(f'Попытка №{user_try}: ').lower()

    if user_word == word:
        print(f'Верно! Это слово {word.upper()}')
        is_guess = True
        break
    elif is_word(user_word, words_data):
        print(get_feedback(user_word, word))
        user_try += 1
    else:
        print('Такого слова нет!')

    print()

if not is_guess:
    print(f'Это было слово {word}')
