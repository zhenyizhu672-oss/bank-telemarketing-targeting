import pandas as pd

df = pd.read_csv('data/bank-full.csv', sep=';')

print('===== 1. 数据规模 =====')
print(df.shape)

print('\n===== 2. 列名和数据类型 =====')
print(df.dtypes)

print('\n===== 3. 每列的空值数量 =====')
print(df.isnull().sum())

print('\n===== 4. 每列里 "unknown" 的数量 =====')
print((df == 'unknown').sum())

print('\n===== 5. 目标变量 y 的分布 =====')
print(df['y'].value_counts())

print('\n===== 6. poutcome 为 unknown 的人，以前被联系过吗？ =====')
print(pd.crosstab(df['poutcome'], df['previous'] == 0))

print('\n===== 7. contact 为 unknown 的记录集中在哪些月份？ =====')
print(pd.crosstab(df['month'], df['contact'] == 'unknown'))

print('\n===== 8. 各联系方式的转化率 (%) =====')
print(df.groupby('contact')['y'].apply(lambda s: (s == 'yes').mean() * 100).round(1))
