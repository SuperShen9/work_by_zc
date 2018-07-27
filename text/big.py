# -*- coding: utf-8 -*-
# author：Super.Shen
import pandas as pd

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

file = 'C:\\Users\Administrator\Desktop\\text\\BIG.xlsx'
df = pd.read_excel(file)

print(df.head())
print('\n')
# print(df.info())

# exit()
df = df.groupby('选择方案').size()
# df.reset_index(inplace=True)
# print(df.index)
print(df)