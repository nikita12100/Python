import argparse
import re
import sys

#запись модели в файл
def write_model(words, out_path):
    with open(out_path + 'model.txt', 'a') as wr:
        for i in range(len(words) - 1):  # идем по всем словам , кроме поледнего, тк у него нет пары
            wr.write(words[i] + ' ' + words[i + 1] + '\n')  # записавыем пары слов


# создание модели
# в модели храниятся пары слов, пары могут дублироватья
# подсчет количества вхождений пар в "genereate"
def make_model(in_path, low_case, out_path):
    if args.input is not None:
        f = open(args.input + 'input.txt', 'r')
    else:
        f = sys.stdin

    last = '_'  # соединяем последнее слово с первым
    for line in f:  # читаем из файла
        line = re.sub('[^a-zA-Zа-яА-Я ]+', '', line) # очистили от неалфавитных символов
        if low_case:  # приводим  к lowercase, если надо
            line = line.lower()

        words = line.split()  # множество пар

        words.insert(0, last)
        last = words[-1]
        write_model(words, out_path)

    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Путь к директории, в которой лежит коллекция документов.Файл должен называться "input.txt" !')
    parser.add_argument('--model', help='Путь к файлу, в который сохраняется модель. Имя модели должно быть "model.txt" !')
    parser.add_argument('--lc', action='store_true', help='Приводить ли текст к нижнему ригистру ? (0 - нет, 1 - да)')
    args = parser.parse_args()
    # аргументы

    words = make_model(args.input, args.lc, args.model)