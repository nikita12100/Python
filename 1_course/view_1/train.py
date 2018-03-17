import argparse
import re
import fileinput


# создание модели
# в модели храниятся пары слов
# пары могут дублироватья
# подсчет количества вхождений пар в "genereate"
def make_model(in_path, low_case, out_path):
    with open(in_path, 'r') as rd, open(out_path, 'w') as wr:
        for line in rd:  # читаем из файла
            line = line.strip()  # убрали пробелы сначала и с конца
            reg = re.compile('[^a-zA-Zа-яА-Я ]')  # очистили от неалфавитных
            line = reg.sub('', line)  # и тут тоже
            if low_case == 1:  # приводим  к lowercase, если надо
                line = line.lower()

            words = line.split()  # множество пар
            # прочитали из файла

            for i in range(len(words) - 1):  # идем по всем словам , кроме поледнего, тк у него нет пары
                wr.write(words[i] + ' ' + words[i + 1] + '\n')  # записавыем пары слов


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='Путь к директории, в которой лежит коллекция документов.')
    parser.add_argument('--model', help='Путь к файлу, в который сохраняется модель.')
    parser.add_argument('--lc', action='store_true', help='Приводить ли текст к нижнему ригистру ? (0 - нет, 1 - да)')
    args = parser.parse_args()
    # аргументы

    if args.input is not None:
        words = make_model(args.input, args.lc, args.model)
    else:
        words = make_model(fileinput.input(), args.lc, args.model)
