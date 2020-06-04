import pandas as pd
import random
import product

# parameters
# salary
citizen_salary_parameter1 = 3
citizen_salary_parameter2 = 10

# параметры для отбора продукта
max_price = 10000
min_qv = 0

# класс потребителя
class citizen:
    def __init__(self, id=0):
        self.id = id
        # стартовый капитал
        self.money = self.set_salary()

    # задаём схему по которой человек будет получать зарплату
    # все схемы на основе генератора случайных чисел
    def set_salary(self):
        # "коммунизм", у всех одинаковое случайное число
        #  return round(random.randint(10, 100),2)
        # "развитой социализм", нормальное распределение, у большиснтва средняя зарплата
        # return round(random.normalvariate((100-10)/2, 10),2)
        # "современное общество", есть длинный правый хвост
        return round(random.gammavariate(citizen_salary_parameter1, citizen_salary_parameter2), 2)

    # функция потребления продуктов
    # берём то, что можем позволить по деньгам
    # берём самый качественный, который можем
    # при равном качестве тот, что дешевле
    def consume(self, products):
        # возвращать будем продукт
        fun_result = product.product(id=-1)
        available_product_lst = []
        # цикл для фильтрации тех, что не карману
        for pr in products:
            if self.money >= pr.price:
                available_product_lst.append(pr)

        best_price = max_price
        best_qv = min_qv
        # цикл поиска лучшего качества
        for pr in available_product_lst:
            if pr.quality >= best_qv:
                best_qv = pr.quality

        product_qv_lst = []
        # сбор всех продуктов лучшего качества
        for pr in available_product_lst:
            if pr.quality == best_qv:
                product_qv_lst.append(pr)

        # выбор из них тех, что дешевле
        for pr in product_qv_lst:
            if pr.price <= best_price:
                best_price = pr.price

        # вывод продукта с лучшими характеристиками
        for pr in product_qv_lst:
            if pr.price == best_price:
                fun_result = pr
                break

        return fun_result

        # отображаем все параметры в виду dataframe

    def to_df(self):
        df = pd.DataFrame(data=[self.__dict__.values()], columns=self.__dict__.keys())
        return df

