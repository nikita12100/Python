import argparse
import random


def Read_Model(path):  # восстановили словарь
    pairs = {}
    f = open(path, 'r')
    for i in f:
        s = i.split('=')
        pairs[((s[0].split())[0], (s[0].split())[1])] = int(s[1][:2])
    f.close()
    return pairs


def Build_Sentence(pairs, seed):
    result = ''
    for i in range(int(args.length)):  # идем по всем парам
        result += seed + ' '  # записываем наше слово
        frequency = []  # следующие слова за seed
        for words in pairs:
            if words[0] == seed:  # нашли пару с seed-world[]
                for k in range(pairs.get(words)):
                    frequency.append(
                        words[1])  # записываем в freq слова следующие за seed(солько , сколько вхождений пар)
        seed = random.choice(frequency)  # выбираем следующее
    return result


def Write_Result(path, result):
    w = open(path, 'w')
    w.write(result)
    w.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='Путь к файлу, из которого загружается модель.')
    parser.add_argument('--seed', help='Начальное слово.')
    parser.add_argument('--length', help='Длина последовательности.')
    parser.add_argument('--output', help='Файл, в который будет записан результат.')
    args = parser.parse_args()
    # аргументы

    pairs = Read_Model(args.model)

    seed = ''
    keys = pairs.keys()  # выбираем слово с которого начнем посторение
    if args.seed != None:
        seed = args.seed
    else:
        for i in pairs:  # вытаскмваем первый ключ
            seed = i[0]
            break

    result = Build_Sentence(pairs, seed)

    if args.output != None:
        Write_Result(args.output, result)
    else:
        print(result)
