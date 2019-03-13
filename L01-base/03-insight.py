# -*- coding: utf-8 -*-
#
# 数据探索
# Author: alex
# Created Time: 2019年03月08日 星期五 15时58分11秒
import pandas as pd
import matplotlib.pyplot as plt

dataset_filename = '../datasets/boston.csv'

# 读取数据集
df = pd.read_csv(dataset_filename)

# 计算特征与目标的相关性
# 小数据集可以这样计算
corr = df.corr()
print(corr['target'].sort_values(ascending=False))

# 相关性散点图
df.plot(kind='scatter', x='RM', y='target', alpha=0.1)
plt.show()
df.plot(kind='scatter', x='CHAS', y='target', alpha=0.1)
plt.show()
df.plot(kind='scatter', x='LSTAT', y='target', alpha=0.3)
plt.show()
