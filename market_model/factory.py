import pandas as pd
import numpy as np
import random
import datetime
import product as product


# разброс расходов
max_cost = 100
min_cost = 5

# разброс качества
max_qv = 30
min_qv = 2

# разброс капитала
cap_avarage = 1000
cap_disp = 300

# разброс инвестиций
capital_average = -100
capital_disp = 50

# разброс изменений себестоимости
cost_average = 0
cost_disp = 5

# разброс изменений качества
qv_average = 0
qv_disp = 3

# класс фабрики
class factory:
    def __init__(self, id=-1):
        # id
        self.id = id
        # предел качества продукта, меньше - можно
        self.max_quality = self.set_params()[0]
        # себестоимость
        self.cost = self.set_params()[1]
        # деньги у завода
        self.capital = self.set_params()[2]
        # продажи текущего периода
        self.pur = 0
        # цена продажи текущего периода
        self.price = 0
        self.capital_history = []
        self.cost_history = []
        self.quality_history = []
        self.pur_history = []
        self.price_history = []
        self.history = pd.DataFrame()

    def set_params(self):
        max_quality = round(random.randint(min_qv, max_qv), 0)
        selcost = round(random.randint(min_cost, max_cost), 2)
        capital = round(random.normalvariate(cap_avarage, cap_disp), 2)

        return max_quality, selcost, capital

    # функция проверки кредитоспособности
    def check(self):
        if self.capital <= 0:
            return -1
        else:
            return 0

    #  функция производтсва
    def produce(self, product_id, price, quality):
        # если норм по капиталам, себестоимости и производственным мощностям, то вперёд
        if (price > self.cost) and (quality <= self.max_quality) and (self.check() == 0):
            self.price = price
            return product.product(id=product_id, quality=quality, price=price)
        else:
            self.price = -10000
            return product.product(id=-1)

    # функкция сделки
    def trade(self):
        # расходы на производство считаем здесь, чтобы не заморачиваться пока остатками
        self.capital = self.capital - self.cost
        if self.check() == 0:
            # поднимаем счётчики
            self.pur = self.pur + 1
            self.capital = self.capital + self.price
        else:
            pass

    # храним историю продаж, запускаем в конце цикла
    def hist(self):  # , period):
        self.capital_history.append(self.capital)
        self.cost_history.append(self.cost)
        self.quality_history.append(self.max_quality)
        self.pur_history.append(self.pur)
        self.price_history.append(self.price)

    def get_modern_params(self):
        capital_addon = round(random.normalvariate(capital_average, capital_disp), 2)
        # костыль на случай отрицательных инвестиций
        if capital_addon > 0:
            capital_addon = -10
        cost_addon = round(random.normalvariate(cost_average, cost_disp), 2)
        qv_addon = round(random.normalvariate(qv_average, qv_disp), 0)

        return qv_addon, cost_addon, capital_addon

    def modernise_proces(self, qv_addon, cost_addon, capital_addon):
        if (self.capital + capital_addon > 0):
            if self.max_quality + qv_addon > 0:
                self.max_quality = np.round(self.max_quality + qv_addon, 0)
            if self.cost + cost_addon > 0:
                self.cost = np.round(self.cost + cost_addon, 2)
            self.capital = np.round(self.capital + capital_addon, 2)
        else:
            pass

    # функция модернизации
    def modernise(self):
        # получили параметры модернизации
        qv_addon, cost_addon, capital_addon = self.get_modern_params()

        # если раунд не первый, то
        if len(self.pur_history) > 1:
            # если сейчас продаж нет, а раньше были, то откатываемся
            if (self.pur_history[-1] == 0) & (self.pur_history[-2] > 0):
                #                 print(self.id, ': 1')
                self.max_quality = self.quality_history[-2]
                self.cost = self.cost_history[-2]
            # иначе модернизируемся
            else:
                #                 print(self.id, ': 2')
                self.modernise_proces(qv_addon, cost_addon, capital_addon)
        # на первом раунде все модернизируются
        else:
            #             print(self.id, ': 3')
            self.modernise_proces(qv_addon, cost_addon, capital_addon)

    def to_null(self):
        # обнуляем счётчики текущего цикла
        self.price = 0
        self.pur = 0

    # отображаем все параметры в виду dataframe
    def to_df(self):
        df = pd.DataFrame(data=[self.__dict__.values()], columns=self.__dict__.keys())
        df = df.drop(columns=['history'])
        return df
