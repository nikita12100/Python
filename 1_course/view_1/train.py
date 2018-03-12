import argparse
import re
import fileinput


def Read(path, low_case):  # чтение файла, и возвращаем лист всех слов(с повторениями)
    words = []  # сам список слов

    f = open(path, 'r')
    for line in f:
        line = line.strip()  # убрали пробелы сначала и с конца
        reg = re.compile('[^a-zA-Zа-яА-Я ]')  # очистили от неалфавитных
        line = reg.sub('', line)  # и тут тоже
        if low_case == 1:  # приводим  к lowercase, если надо
            line = line.lower()

        words += line.split()
    f.close()
    return words


def Count_Pairs(words): #подсчет количства пар, запись в словарь
    count_pairs = {}    # словарь пар, ключ - пара, значение - количество вхождений
    for i in range(len(words) - 1):     # идем по всем словам , кроме поледнего, тк у него нет пары
        if (words[i], words[i + 1]) in count_pairs:   # если пара есть, то увеличиваем счетчик
            count_pairs[(words[i], words[i + 1])] += 1
        else: # елси пары нет, то добавляем
            count_pairs[(words[i], words[i + 1])] = 1
    return count_pairs


def Write(path, count_pairs):    #запись модели
    w = open(path, 'w')
    for i in count_pairs:        # первое слово пары, второе , и количетво пар
        w.write(i[0] + ' ' + i[1] + '=' + str(count_pairs[i]) + '\n')
    w.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Путь к директории, в которой лежит коллекция документов.')
    parser.add_argument('--model', help='Путь к файлу, в который сохраняется модель.')
    parser.add_argument('--lc', action='store_true', help='Приводить ли текст к нижнему ригистру ? (0 - нет, 1 - да)')
    args = parser.parse_args()
    # аргументы

    if args.input != None:
        words = Read(args.input, args.lc)
    else:
        words = Read(fileinput.input(), args.lc)

    count_pairs = Count_Pairs(words)

    Write(args.model, count_pairs)
