#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime


def display_file_info(folder_path):
    # Получаем список файлов в папке
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    print("Информация о файлах:")
    for file in files:
        file_path = os.path.join(folder_path, file)

        # Получаем информацию о файле
        file_info = {
            'File Name': file,
            'Size (bytes)': os.path.getsize(file_path),
            'Last Modified': datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        }

        # Выводим информацию о файле
        print(file_info)


if __name__ == "__main__":
    folder_path = './индивдульное 3'  # Путь к папке с файлами

    try:
        display_file_info(folder_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

