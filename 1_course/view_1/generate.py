import argparse
import random
import os


# считывание пар слов
# подсчет их количства
# возвращаем словарь вида
# (<слово1>,<слово2>) <количество вхождений>
def read_model(path):  # восстановили словарь
    pairs = {}
    with open(path, 'r') as f:
        for line in f:
            s = line.split()  # полчучаем пару
            pairs[s[0], s[1]] = int(s[2])  # если нет, то добавляем

    return pairs  # возвращаем словарь


# получаем словарь и начальное слово
# возвразаем итоговое предложение
def build_sentence(pairs, seed):
    result = ''
    for i in range(int(args.length)):  # идем по всем парам
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
    parser.add_argument('--model', help='Путь к файлу, из которого загружается модель. Имя модели должно быть "model.txt" !')
    parser.add_argument('--seed', help='Начальное слово.')
    parser.add_argument('--length', help='Длина последовательности.')
    parser.add_argument('--output', help='Файл, в который будет записан результат.')
    args = parser.parse_args()
    # аргументы

    pairs = read_model(os.path.join(args.model, 'model.txt'))

    seed = ''
    if args.seed is not None:
        seed = args.seed
    else:
        seed = random.choice(list(pairs))[0]

    result = build_sentence(pairs, seed)

    if args.output is not None:
        write_result(args.output, result)
    else:
        print(result)
