import argparse
import re
import sys
import os
import collections


# запись модели в файл
def write_model(out_path, counter):
    with open(os.path.join(out_path, 'model.txt'), 'a') as wr:
        for i in set(counter.elements()):
            wr.write((i[0] + ' ' + i[1] + ' ' + str(counter[i]) + '\n'))


# создание модели
# в модели храниятся пары слов, пары могут дублироватья
# подсчет количества вхождений пар в "genereate"
def make_model(in_path, low_case, out_path, counter):
    if args.input is not None:
        f = open(in_path, 'r')
    else:
        f = sys.stdin

    last = '_'  # соединяем последнее слово с первым
    for line in f:  # читаем из файла
        line = re.sub('[^a-zA-Zа-яА-Я ]+', '', line)  # очистили от неалфавитных символов
        if low_case:  # приводим  к lowercase, если надо
            line = line.lower()

        words = line.split()  # множество пар

        words.insert(0, last)
        last = words[-1]

        for i in range(len(words) - 1):  # идем по всем словам , кроме поледнего, тк у него нет пары
            counter[(words[i], words[i + 1])] += 1  # считаем повторения пар

    if out_path is not None:
        write_model(out_path, counter)
    else:
        write_model(os.getcwd(), counter)  # записываем в текущюю директорию

    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        help='Путь к директории, в которой лежит коллекция документов.')
    parser.add_argument('--model',
                        help='Путь к файлу, в который сохраняется модель. По умолчанию название файла "model.txt".')
    parser.add_argument('--lc', action='store_true', help='Приводить ли текст к нижнему ригистру ? (0 - нет, 1 - да)')
    args = parser.parse_args()
    # аргументы

    counter = collections.Counter()

    # работа с директорий в которой лежит каталог
    if args.input is not None:  # если есть директория то перебираем все файлы в ней
        dir_files = [f.name for f in os.scandir(args.input) if f.is_file()]
        for file in dir_files:
            make_model(os.path.join(args.input, file), args.lc, args.model, counter)
        dir_folder = [f.name for f in os.scandir(args.input) if not f.is_file()]
        if dir_folder:  # если есть вложенные папки
            for folder in dir_folder:
                foler_files = [f.name for f in os.scandir(os.path.join(args.input, folder)) if f.is_file()]
                for file in foler_files:
                    make_model(os.path.join(args.input, folder, file), args.lc, args.model, counter)
    else:
        make_model(args.input, args.lc, args.model, counter)
