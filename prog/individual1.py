#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

def words_start_and_end_with_vowels(text):
    words = text.split()
    valid_words = []

    for word in words:
        # Определяем, начинается ли слово с гласной буквы
        starts_with_vowel = is_vowel(word[0])

        # Определяем, заканчивается ли слово гласной буквой
        ends_with_vowel = is_vowel(word[-1])

        if starts_with_vowel and ends_with_vowel:
            valid_words.append(word)

    return valid_words

if __name__ == "__main__":
    file_path = 'ind1.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            valid_words = words_start_and_end_with_vowels(text) #доупстимые слова

            print("Words starting and ending with vowels:")
            for word in valid_words:
                print(word)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
