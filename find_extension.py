"""Программа поиска расширений в лог-файле"""
import time
import re


def find_ext(input_file):
    """Функция поиска расширений в лог-файле"""
    dir_log = open(input_file, mode='r', encoding='utf8')
    sort_list = open('output/sort_list_' +
                     str(time.strftime("%Y_%m_%d_%H_%M_%S")) +
                     '.txt', 'tw')

    for line in dir_log:
        match = re.findall(r'\.[a-zA-Z]{2,5}', line)
        sort_list.writelines(set(match))
        sort_list.write('\n')

    dir_log.close()
    sort_list.close()


find_ext('input/dir_log.txt')
