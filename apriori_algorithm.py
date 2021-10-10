# coding: utf-8 -*-
# author: 梁开孟
# date：2021/10/10 0010 19:48

import warnings
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules

warnings.filterwarnings("ignore")
pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

class AprioriRulesAlgorithm(object):
    def __init__(self, filename):
        data = self.load_data(filename)
        baskets = self.combine_product(data)
        df = self.transaction_encoder(baskets)
        rules = self.calculation_target(df)
        print(rules)

    def load_data(self, filename):
        return pd.read_csv(filename, encoding="gbk")

    def combine_product(self,
                        product_table,
                        key="OrderNumber",
                        sale_product="Model"):
        baskets = product_table.groupby(key)[sale_product].apply(lambda product: product.tolist())
        baskets = baskets.tolist()
        return baskets

    def transaction_encoder(self, baskets):
        """
        @function：转换为算法可接受模型（布尔值），原理为独热编码
        @param baskets: 订单合并后的数组
        @return:独热编码后的数据帧pandas.DataFrame
        """
        transaction = TransactionEncoder()
        baskets = transaction.fit_transform(baskets)
        df = pd.DataFrame(baskets, columns=transaction.columns_)
        return df

    def calculation_target(self,
                           dataframe,
                           min_support=0.01,
                           use_colnames=True,
                           min_threshold=0.15):
        # 设置支持度求频繁项集
        frequent_itemsets = apriori(dataframe, min_support=min_support, use_colnames=use_colnames)
        # 求关联规则,设置最小置信度为0.15
        rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=min_threshold)
        # 设置最小提升度
        # rules = rules.drop(rules[rules.lift <1.0].index)
        columns = ['antecedents', 'consequents', 'support', 'confidence', 'lift', 'leverage', 'conviction']
        rules = rules[columns]
        return rules.sort_values(by=["lift"], ascending=False)

if __name__ == "__main__":
    filename = "data/bike_data.csv"
    AprioriRulesAlgorithm(filename)