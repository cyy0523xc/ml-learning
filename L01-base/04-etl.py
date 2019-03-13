# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2019年03月13日 星期三 00时31分39秒
import pandas as pd
from sklearn.preprocessing import Imputer

dataset_filename = '../datasets/housing.csv'

# 读取数据集
df = pd.read_csv(dataset_filename)
df.info()
print("可以看到total_bedrooms字段有缺失值")

print("处理缺失值的方式：")
df.dropna(subset=['total_bedrooms']).info()
# axis: {0 or 'index', 1 or 'columns'}, default 0
# 可以按行或者列来删除
df.drop('total_bedrooms', axis="columns").info()
# 使用中位数填充
df2 = pd.DataFrame(df)
median = df['total_bedrooms'].median()
df2['total_bedrooms'] = df['total_bedrooms'].fillna(median)
df2.info()

# Imputer: 可以用于全局缺失值处理
print("Imputer: 可以用于全局缺失值处理:")
imputer = Imputer(strategy="median")
# 需要先删除非数值字段
df2 = df.drop('ocean_proximity', axis='columns')
# fit: 估算器
# transform: 转换器
X = imputer.fit_transform(df2)
df3 = pd.DataFrame(X, columns=df2.columns)
df3.info()


