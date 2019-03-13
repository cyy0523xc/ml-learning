# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2019年03月08日 星期五 14时41分20秒
import pandas as pd
import matplotlib.pyplot as plt


dataset_filename = '../datasets/boston.csv'

# 读取数据集
df = pd.read_csv(dataset_filename)

# 查看数据集的基本情况
df.info()

# 查看数据集的前若干行
df.head()

# 查看数值属性的摘要信息
df.describe()

# 查看某字段的数值分布
df['target'].value_counts()

# 数值属性直方图
# %matplotlib inline
# @bins: 直方的数量
df.hist(bins=50, figsize=(20, 10))
plt.show()
