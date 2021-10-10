# coding: utf-8 -*-
# author: 梁开孟
# date：2021/10/10 0010 19:02

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules

pd.set_option("display.width", 500)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 500)

bike = pd.read_csv("data/bike_data.csv", encoding="gbk")

baskets =bike.groupby('OrderNumber')['Model'].apply(lambda x: x.tolist())
baskets = list(baskets)

#转换为算法可接受模型（布尔值）
te = TransactionEncoder()
baskets_tf = te.fit_transform(baskets)
df = pd.DataFrame(baskets_tf,columns=te.columns_)
#设置支持度求频繁项集
frequent_itemsets = apriori(df, min_support=0.01, use_colnames= True)
#求关联规则,设置最小置信度为0.15
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.1)
#设置最小提升度
# rules = rules.drop(rules[rules.lift <1.0].index)
#设置标题索引并打印结果
rules.rename(columns = {'antecedents': 'lhs',
                        'consequents': 'rhs',
                        'support': 'Support',
                        'confidence': 'Confidence'}, inplace = True)
rules = rules[['lhs','rhs','Support','Confidence','lift']]
print(rules)
