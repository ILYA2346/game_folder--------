"""Функции для игры «Виселица на поле чудес» (версия 3)."""
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORDS_FILE = os.path.join(BASE_DIR, "words.txt")
STAGE_FILES = [
    os.path.join(BASE_DIR, "gallows", "stage_01.txt"),
    os.path.join(BASE_DIR, "gallows", "stage_02.txt"),
    os.path.join(BASE_DIR, "gallows", "stage_03.txt"),
    os.path.join(BASE_DIR, "gallows", "stage_04.txt"),
    os.path.join(BASE_DIR, "gallows", "stage_05.txt"),
    os.path.join(BASE_DIR, "gallows", "stage_06.txt"),
    os.path.join(BASE_DIR, "gallows", "stage_7.txt"),
]
MASK = "■"
YES_ANSWERS = ["да", "д", "yes", "y"]


def show_message(msg):
    """Выводит сообщение на экран."""
    print(msg)


def prompt(msg):
    """Спрашивает у игрока строку."""
    return input(msg)


def load_words():
    """Читает слова с описаниями из файла. Возвращает словарь слово -> описание."""
    words = {}
    try:
        with open(WORDS_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except OSError:
        show_message("Не удалось прочитать файл со словами: " + WORDS_FILE)
        return words
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 2:
            words[parts[0].strip().lower()] = parts[1].strip()
    return words


def has_words(words):
    """Остались ли ещё слова."""
    return len(words) > 0


def pick_word(words):
    """Выбирает случайное слово."""
    return random.choice(list(words.keys()))


def get_description(words, word):
    """Возвращает описание слова."""
    return words[word]


def remove_word(words, word):
    """Удаляет слово из словаря, чтобы оно не повторялось."""
    words.pop(word)


def get_lives():
    """Жизней столько же, сколько частей у виселицы."""
    return len(STAGE_FILES)


def is_alive(lives):
    return lives > 0


def decrease_lives(lives):
    return lives - 1


def create_table(word):
    """Создаёт список из закрытых символов по длине слова."""
    return [MASK] * len(word)


def open_letter(table, word, letter):
    """Открывает все позиции, где стоит буква."""
    for i in range(len(word)):
        if word[i] == letter:
            table[i] = letter
    return table


def open_word(word):
    """Открывает слово целиком."""
    return list(word)


def is_word_correct(word, answer):
    return word == answer


def is_right_letter(word, answer):
    """Ответ — одна буква, и она есть в слове."""
    return len(answer) == 1 and answer in word


def is_table_complete(table):
    """Все буквы открыты."""
    return MASK not in table


def prompt_answer():
    """Спрашивает букву или слово, пустой ввод не принимает."""
    answer = ""
    while answer == "":
        answer = prompt("Назовите букву или слово целиком: ").strip().lower()
    return answer


def prompt_replay():
    return prompt("Сыграть ещё? (да/нет): ").strip().lower()


def is_yes(answer):
    return answer in YES_ANSWERS


def show_table(table):
    show_message(" ".join(table).upper())


def show_description(description):
    show_message(description)


def show_gallows(lives):
    """Рисует виселицу из файла: чем меньше жизней, тем больше частей."""
    index = len(STAGE_FILES) - lives - 1
    try:
        with open(STAGE_FILES[index], "r", encoding="utf-8") as f:
            show_message(f.read())
    except (OSError, IndexError):
        show_message("(не удалось прочитать файл виселицы: " + STAGE_FILES[index] + ")")


def show_wrong():
    show_message("Неправильно. Вы теряете жизнь")


def show_win():
    show_message("Вы выиграли! Приз в студию!")


def show_lose(word):
    show_message("Вы проиграли. Было загадано слово: " + word.upper())


def show_finish(words):
    if has_words(words):
        show_message("Игра окончена. До встречи!")
    else:
        show_message("Слова закончились. Спасибо за игру!")