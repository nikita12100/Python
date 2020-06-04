import pandas as pd


# класс продукта
class product:
    def __init__(self, id=-1, quality=-100, price=-10000):
        self.id = id
        self.quality = quality
        self.price = price

    # отображаем все параметры в виду dataframe
    def to_df(self):
        df = pd.DataFrame(data=[self.__dict__.values()], columns=self.__dict__.keys())
        return df
