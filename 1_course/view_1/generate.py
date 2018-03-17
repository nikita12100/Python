import argparse
import random


# считывание пар слов
# подсчет их количства
# возвращаем словарь вида
# (<слово1>,<слово2>) <количество вхождений>
def read_model(path):  # восстановили словарь
    pairs = {}
    with open(path, 'r') as f:
        for i in f:
            s = i.split()  # полчучаем пару
            if (s[0], s[1]) in pairs:  # если уже есть, то увеличиваем счетчик
                pairs[s[0], s[1]] += 1
            else:
                pairs[s[0], s[1]] = 1  # если нет, то добавляем

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
                for k in range(pairs.get(words)):
                    frequency.append(
                        words[1])  # записываем в freq слова следующие за seed(солько , сколько вхождений пар)
        seed = random.choice(frequency)  # выбираем следующее
    return result


def write_result(path, result):
    with open(path, 'w') as w:
        w.write(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='Путь к файлу, из которого загружается модель.')
    parser.add_argument('--seed', help='Начальное слово.')
    parser.add_argument('--length', help='Длина последовательности.')
    parser.add_argument('--output', help='Файл, в который будет записан результат.')
    args = parser.parse_args()
    # аргументы

    pairs = read_model(args.model)

    seed = ''
    keys = pairs.keys()  # выбираем слово с которого начнем посторение
    if args.seed is not None:
        seed = args.seed
    else:
        for i in pairs:  # вытаскмваем первый ключ
            seed = i[0]
            break

    result = build_sentence(pairs, seed)

    if args.output is not None:
        write_result(args.output, result)
    else:
        print(result)
