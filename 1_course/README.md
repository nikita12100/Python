# Python

MIPT Python course task.

## view_1

### Программа состоит из двух частей `generate.py` и `train.py`.

В `generate.py` мы получаем сырой текст и строим словарь: `word1 word2 #count` в файле *model.txt*. 

Аргументы:

```
    input   --- Путь к директории, в которой лежит коллекция документов.
    model   --- Путь к файлу, в который сохраняется модель. Пример : C:\model.txt
    lc      --- Приводить ли текст к нижнему ригистру ? (0 - нет, 1 - да)
```

В  `train.py` мы получаем модель, и по заданному слову `seed` продолжаем предложение длиной `length` слов. И записываем результат в `output`.

Программе в качастве аргументов подается:

```
  model  --- Путь к файлу, из которого загружается модель.
  seed   --- Начальное слово.
  length --- Длина последовательности.
  output --- Файл, в который будет записан результат.
```

