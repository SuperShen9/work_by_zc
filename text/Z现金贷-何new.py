# -*- coding: utf-8 -*-
# author：Super.Shen

import os
import pandas as pd
from Daily.Func import yue, ri, ri_now
import datetime
hour = datetime.datetime.now().strftime('%H')
if len(yue) < 2:
    yue = '0' + yue
if len(ri_now) < 2:
    ri_now = '0' + ri_now
if len(ri) < 2:
    ri = '0' + ri

filepath = 'D:\Super\\每日报告合并'

# 切换路径
os.chdir(filepath)
df = pd.DataFrame()

list1 = []
for x, y, excels in os.walk(filepath):
    len_cs = len(excels)
    for excel in excels:
        df1 = pd.read_excel(excel)
        # print(excel,';列长度:{}'.format(df1.shape[1]))
        df = df.append(df1)
        list1.append(excel.split('-')[1])
        # print(excel.split('-')[1])

df = df[df['姓名'].notnull()]
df.fillna(value=0, inplace=True)
df = df.reset_index(drop=True)

ii = df.shape[0] + 1
for x, y in df.groupby(['时间']):
    y = y.reset_index(drop=True)
    print(y)
    exit()
    df.loc[ii, '姓名'] = y.loc[0, '时间']
    for col in y.columns[2:]:
        df.loc[ii, col] = y[col].sum()
    ii += 1

df = df[df['时间'].isnull()]


if int(hour) > 10:
    df.to_excel('C:\\Users\Administrator\Desktop\现金贷催收{}月{}日报告2.xlsx'.format(yue, ri_now), index=False)
else:
    df.to_excel('C:\\Users\Administrator\Desktop\现金贷催收{}月{}日报告2.xlsx'.format(yue, ri), index=False)
print('\n没有问题，统计已存放桌面！')

