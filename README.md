# 关联规则算法

关联规则(Association Rules)是反映一个事物与其他事物之间的相互依存性和关联性，是数据挖掘的一个重要技术，用于从大量数据中挖掘出有价值的数据项之间的相关关系。

## 频繁项集评估标准
* 支持度：几个关联的数据在数据集中出现的次数占总数据集的比重。
$$Support(X,Y)=P(XY)=\frac{number(XY)}{num(ALLSamples})$$
* 置信度：一个数据出现后，另一个数据出现的概率，或者说数据的条件概率。
$$Confidence(X\Leftarrow{Y})=P(X|Y)=P(XY)/P(Y)$$
* 提升度：表示含有Y的条件下，同时含有X的概率，与X总体发生的概率之比。
$$Lift(X\Leftarrow{Y})=P(X|Y)/P(X)=Confidence(X\Leftarrow{Y})/P(X)$$
