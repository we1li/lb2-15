#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def generate_password(word_list):
    # Выбираем два случайных слова из списка
    word1 = random.choice(word_list)
    word2 = random.choice(word_list)

    # Проверяем, что слова удовлетворяют условиям по длине
    while len(word1) < 3 or len(word2) < 3:
        word1 = random.choice(word_list)
        word2 = random.choice(word_list)

    # Формируем пароль, объединяя первые буквы слов и делаем заглавными
    password = word1[0].upper() + word1[1:] + word2[0].upper() + word2[1:]

    return password

if __name__ == "__main__":
    file_path = 'ind2.txt'  # Путь к файлу со списком слов

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Читаем список слов из файла
            word_list = [line.strip() for line in file if len(line.strip()) >= 3]

            # Генерируем пароль
            password = generate_password(word_list)

            print("Generated password:", password)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
