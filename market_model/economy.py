import pandas as pd
import citizen as citizen
import product as product
import factory as factory

# тестовая функция
def test():
    print('working')

# функции рынка, то есть встречи потребителей и продуктов
def global_produce(fact_lst):
    products = []
    for f in fact_lst:
        if f.check() == 0:
            product = f.produce(product_id=f.id, price=f.cost + 1, quality=f.max_quality)
            products.append(product)

    return products


def global_consume(cit_lst, products):
    products_to_trade = []
    for cit in cit_lst:
        product = cit.consume(products)
        products_to_trade.append(product)

    return products_to_trade


def global_trade(goods_to_trade, fact_lst):
    for good in goods_to_trade:
        if good.id >= 0:
            fact_lst[good.id].trade()


def global_posttrade(fact_lst):
    for fact in fact_lst:
        fact.hist()
        fact.to_null()
        fact.modernise()


def market_period(cit_lst, fact_lst, period):
    products_to_consume = global_produce(fact_lst)
    goods_to_trade = global_consume(cit_lst, products_to_consume)

    cit_df = pd.DataFrame()
    for i in range(len(goods_to_trade)):
        good = goods_to_trade[i].to_df()
        good['citizen_id'] = i
        good['money'] = cit_lst[i].money
        cit_df = pd.concat([cit_df, good])

    cit_df['period'] = period

    global_trade(goods_to_trade, fact_lst)

    fact_df = pd.DataFrame()
    for fact in fact_lst:
        fact_df = pd.concat([fact_df, fact.to_df()])

    fact_df = fact_df[['id', 'max_quality', 'cost', 'capital', 'pur', 'price']]
    fact_df['period'] = period

    global_posttrade(fact_lst)

    return cit_df, fact_df


def model(cit_lst, fact_lst, R):
    print('Modelling started')

    cit_df = pd.DataFrame()
    fact_df = pd.DataFrame()

    for r in range(R):
        print(datetime.datetime.now(), ': round ', r, ' started')
        cit_df_r, fact_df_r = market_period(cit_lst, fact_lst, r)
        cit_df = pd.concat([cit_df, cit_df_r])
        fact_df = pd.concat([fact_df, fact_df_r])

    print(datetime.datetime.now(), ' :modelling finished')

    return cit_df, fact_df