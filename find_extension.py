"""Программа поиска расширений в лог-файле"""
import time
import re


def find_ext(input_file):
    """Функция поиска расширений в лог-файле"""
    with open(input_file, mode='r', encoding='utf8') as dir_log:
        extensions = set()  # множество для хранения найденных расширений

        for line in dir_log:
            extensions.update(re.findall(r'\.[a-zA-Z]{2,5}', line))

        # сортировка расширений и запись в файл вывода
        filename = f"output/sort_list_{time.strftime('%Y_%m_%d_%H_%M_%S')}.txt"
        with open(filename, 'tw') as sort_list:
            for extension in sorted(extensions):
                sort_list.write(extension[1:] + '\n')  # удаляем точку и записываем в файл

    print(f"Результат записан в файл {filename}")


find_ext('input/dir_log.txt')
