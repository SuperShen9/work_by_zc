# -*- coding: utf-8 -*-
# author：Super.Shen
import os, openpyxl
import pandas as pd

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

file = 'C:\\Users\Administrator\Desktop\\text\\one.xlsx'
out_file = 'C:\\Users\Administrator\Desktop\\run.xlsx'

df = pd.read_excel(file)


for x in range(3,5000):
    # 每日买big
    df.loc[x, '释放总量'] = df.loc[x - 1, '释放总量'] +200000000
    df['释放比率'] = df['释放总量'].pct_change()
    df.loc[x, 'ONE新增'] = df.loc[x-1,'BIG']/2
    df.loc[x,'持有量']=df.loc[x-1,'持有量']+df.loc[x, 'ONE新增']
    df['持有比率'] = df['持有量'] / df['释放总量']
    df['收益'] = 10000000 * df['持有比率']
    df.loc[x,'BIG']=df.loc[x-1,'BIG']+df.loc[x-1,'收益']/5

    # 每日买one
    # df.loc[x, '释放总量'] = df.loc[x - 1, '释放总量'] + 200000000
    # df['释放比率'] = df['释放总量'].pct_change()
    # df.loc[x, 'BIG'] = df.loc[x - 1, 'BIG']
    # df.loc[x-1,'收益'] = 10000000 * df.loc[x-2,'持有量']/df.loc[x-2, '释放总量']
    # df.loc[x, 'ONE新增'] = df.loc[x-1,'收益']*10
    # df.loc[x, '持有量'] = df.loc[x - 1, '持有量'] + df.loc[x, 'ONE新增']

    if df.loc[x,'释放总量']>=20000000000:
        break



df.loc[df.shape[0]+1,'收益']=df['收益'].sum()+(df['BIG'].max()-6000)*5


# print(df)
# exit()

df.to_excel(out_file)