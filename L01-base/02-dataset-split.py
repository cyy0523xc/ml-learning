# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2019年03月08日 星期五 15时28分20秒
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataset_filename = '../datasets/iris.csv'

# 读取数据集
df = pd.read_csv(dataset_filename)

# 随机拆分: random_state
print("第1次split, random_state=2:")
train_set, test_set = train_test_split(df, test_size=0.5, random_state=2)
print(train_set.head())

print("第2次split, random_state=2:")
train_set, test_set = train_test_split(df, test_size=0.5, random_state=2)
print(train_set.head())

print("第3次split:")
train_set, test_set = train_test_split(df, test_size=0.5)
print(train_set.head())

print("第4次split:")
train_set, test_set = train_test_split(df, test_size=0.5)
print(train_set.head())

# 查看特征分布是否均匀
train_set.hist(bins=50, figsize=(20, 10))
plt.show()
test_set.hist(bins=50, figsize=(20, 10))
plt.show()
print("随机split时，特征分布并不一定均匀")

# 分层抽样
# 参数stratify即用来指定按照某一特征进行分层抽样
# 该参数值不能为浮点数
train_set, test_set = train_test_split(df, test_size=0.5,
                                       stratify=df['target'])
train_set.hist(bins=50, figsize=(20, 10))
plt.show()
test_set.hist(bins=50, figsize=(20, 10))
plt.show()
df.target.plot.bar()
plt.show()
