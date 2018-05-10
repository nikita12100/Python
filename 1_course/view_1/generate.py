import argparse
import random
import os


# считывание пар слов
# подсчет их количства
# возвращаем словарь вида
# (<слово1>,<слово2>) <количество вхождений>
def read_model(path):  # восстановили словарь
    pairs = {}
    try:
        with open(path, 'r') as f:
            for line in f:
                source = line.split()  # полчучаем пару
                pairs[source[0], source[1]] = int(source[2])  # если нет, то добавляем
    except IOError as e:
        print('Файл model.txt не найден.')
        exit(0)
    return pairs  # возвращаем словарь


# получаем словарь и начальное слово
# возвразаем итоговое предложение
def build_sentence(pairs, seed, length):
    result = ''
    for i in range(length):  # идем по всем парам
        result += seed + ' '  # записываем наше слово
        frequency = []  # следующие слова за seed
        for words in pairs:
            if words[0] == seed:  # нашли пару с seed-world[]
                for k in range(pairs.get(words)):  # <значиние> раз добавляем в freq <слово2>
                    frequency.append(words[1])
        seed = random.choice(frequency)  # выбираем следующее
    return result


def write_result(path, result):
    with open(path, 'w') as w:
        w.write(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='Путь к файлу, из которого загружается модель.')
    parser.add_argument('--seed', help='Начальное слово.')
    parser.add_argument('--length', type=int, help='Длина последовательности.')
    parser.add_argument('--output', help='Файл, в который будет записан результат.')
    args = parser.parse_args()
    # аргументы

    # путь к модели
    if args.model is not None:
        pairs = read_model(args.model)
    else: # елси путь не указан, то проверяем текущюю дирректорию
        pairs = read_model(os.path.join(os.getcwd(), 'model.txt'))

    # зерно
    seed = ''
    if args.seed is not None:
        seed = args.seed
    else:
        seed = random.choice(list(pairs))[0]

    # длина
    if args.length is not None:
        result = build_sentence(pairs, seed, args.length)
    else:
        result = build_sentence(pairs, seed, 10) # по деф. длина 10
    # вывод
    if args.output is not None:
        write_result(args.output, result)
    else:
        print(result)
