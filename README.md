# 关联规则算法

关联规则(Association Rules)是反映一个事物与其他事物之间的相互依存性和关联性，是数据挖掘的一个重要技术，用于从大量数据中挖掘出有价值的数据项之间的相关关系。

## 频繁项集评估标准
* 支持度：几个关联的数据在数据集中出现的次数占总数据集的比重。
$$Support(X,Y)=P(XY)=\frac{number(XY)}{num(ALLSamples})$$
* 置信度：一个数据出现后，另一个数据出现的概率，或者说数据的条件概率。
$$Confidence(X\Leftarrow{Y})=P(X|Y)=P(XY)/P(Y)$$
* 提升度：表示含有Y的条件下，同时含有X的概率，与X总体发生的概率之比。
$$Lift(X\Leftarrow{Y})=P(X|Y)/P(X)=Confidence(X\Leftarrow{Y})/P(X)$$

## Apriori算法
* 原理  
如果一个项集是频繁项集，则它的所有子集都是频繁项集；  
如果一个集合不是频繁项集，则它的所有父集（超集）都不是频繁项集。  
* 目标  
发现频繁项集：发现满足最小支持度的所有项集。  
发现关联规则：从频繁项集中提取所有高置信度的规则。  

## 数据格式
OrderNumber|LineNumber|Model
-|:-:|-:
cumid51178|1|山地英骑
cumid51178|2|山地车水壶架
cumid51178|3|运动水壶
cumid51184|1|山地英骑
cumid51184|2|山地车水壶架
cumid51184|3|运动水壶
## 具体实现
* 将同一个订单进行合并，输出列表
```python
baskets = product_table.groupby(key)[sale_product].apply(lambda product: product.tolist())
baskets = baskets.tolist()
```
* 独热编码：将数据转为模型可接受的格式
```python
transaction = TransactionEncoder()
baskets = transaction.fit_transform(baskets)
df = pd.DataFrame(baskets, columns=transaction.columns_)
```
* 设置支持度求频繁项集
```python
frequent_itemsets = apriori(dataframe, min_support=0.01, use_colnames=use_colnames)
```
* 求关联规则,设置最小置信度为0.15
```python
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.15)
```
