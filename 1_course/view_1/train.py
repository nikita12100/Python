import argparse
import re
import sys
import os
import collections


# запись модели в файл
def write_model(out_path, count):
    with open(os.path.join(out_path, 'model.txt'), 'a') as wr:
        for i in set(count.elements()):
            wr.write(i[0] + ' ' + i[1] + ' ' + str(count[i]) + '\n')


# создание модели
# в модели храниятся пары слов, пары могут дублироватья
# подсчет количества вхождений пар в "genereate"
def make_model(in_path, low_case, out_path, c):
    if args.input is not None:
        f = open(os.path.join(args.input, 'input.txt'), 'r')
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
            c[(words[i], words[i + 1])] += 1  # считаем повторения пар

    write_model(out_path, c)

    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        help='Путь к директории, в которой лежит коллекция документов.Файл должен называться "input.txt" !')
    parser.add_argument('--model',
                        help='Путь к файлу, в который сохраняется модель. Имя модели должно быть "model.txt" !')
    parser.add_argument('--lc', action='store_true', help='Приводить ли текст к нижнему ригистру ? (0 - нет, 1 - да)')
    args = parser.parse_args()
    # аргументы

    c = collections.Counter()
    make_model(args.input, args.lc, args.model, c)
