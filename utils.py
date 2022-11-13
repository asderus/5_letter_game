import json
import random

WORDS_FILE = 'words.json'
WORDS_DATA_FILE = 'data_words.json'


def get_word():
    """
    Функция возвращает слово для игры из базы слов
    :return: слово для игры
    """
    words = load_words(WORDS_FILE)
    word = random.choice(words)
    return word


def get_words_data():
    """
    Загружает общую базу слов из пяти букв
    :return: база слов
    """
    words = load_words(WORDS_DATA_FILE)
    return words


def load_words(file_name):
    """
    Загружает слова из файла именем file_name
    :param file_name: имя файла
    :return: список слов
    """
    with open(file_name) as file:
        words = json.load(file)

    return words


def is_word(user_word, words):
    """
    Проверяет является ли введенное пользователем слово - словом
    :param user_word: слово пользователя
    :param words: база слов
    :return: True or False
    """
    return user_word in words


def get_feedback(user_word, word):
    """
    Дает обратную связь о том, насколько близко слово пользователя к исходному слову.
    Если буква заглавная - она стоит на своем месте.
    Если буква маленькая - она стоит НЕ на своем месте
    Если вместо буквы звездочка - такой буквы нет в исходном слове
    :param user_word: слово пользователя
    :param word: исходное слово
    :return: отзыв
    """
    check_1 = []

    # Проверка букв на своих местах
    for user_letter, word_letter in zip(user_word, word):

        if user_letter == word_letter:
            check_1.append(user_letter)
        else:
            check_1.append('*')

    check_2 = [letter.upper() for letter in check_1]

    # Проверка букв не на своих местах и повторяющихся букв
    for i, letter in enumerate(user_word):
        if letter == check_1[i] or letter not in word:
            continue
        elif check_1.count(letter) < word.count(letter):
            check_1[i] = letter
            check_2[i] = letter

    return ''.join(check_2)


def print_rules():
    """
    Печатает правила игры
    """
    print('Добро пожаловать в игру 5 букв!')
    print('Цель игры - отгадать слово за 5 попыток')
    print('Если буква стоит на своем месте - она будет заглавной')
    print('Если буква маленькая - она стоит не на своем месте')
    print('Если вместо буквы звездочка - такой буквы нет в слове')
