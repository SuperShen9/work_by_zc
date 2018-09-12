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

print('\n现金贷催收统计人数：{}'.format(len_cs))

# 筛选出不属于昨天的数据
df = df[df['姓名'] != '张三1']

if int(hour) > 10:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri_now))]
    # df = df[df['日期'] == pd.to_datetime('20180903')]
else:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri))]
    # df = df[df['日期'] == pd.to_datetime('20180804')]


df = df.reset_index(drop=True)

df.sort_values(by='阶段', inplace=True)

i = 20
if df.shape[0] != len_cs:
    error = [l for l in list1 if l not in list(df['姓名'])]
    print('\n{} 的日期有问题，请核对!'.format(error))

else:
    # print(df)
    # exit()
    df['阶段'] = df['阶段'].apply(lambda x: x.upper())
    df['阶段'] = df['阶段'].apply(lambda x: x.strip())
    df.sort_values(by='阶段', inplace=True)
    df.fillna(value=0, inplace=True)

    df.loc[len_cs + i, '阶段'] = '汇总:'
    df.loc[len_cs + i, '姓名'] = df['姓名'].count()

    df = df[['日期','阶段','姓名','分单量','停机','关机','空号','设置','未接','拒接','接通单数','总持单量','完结','续期','部分还款','部分还款金额','代扣金额','催回率','催回总金额']]

    for col in df.columns[3:]:
        df.loc[len_cs + i, col] = df[col].sum()

    ii = df.shape[0] + 1
    for x, y in df.groupby(['阶段']):
        y = y.reset_index(drop=True)
        df.loc[ii, '阶段'] = y.loc[0, '阶段']
        df.loc[ii, '姓名'] = y['姓名'].count()
        for col in y.columns[3:]:
            df.loc[ii, col] = y[col].sum()
        ii += 1

    df['催回率'] = (df['完结'] + df['续期'])/df['分单量']


    df = df.reset_index(drop=True)
    df['催回率'].fillna(value=0, inplace=True)
    df.drop(df.shape[0]-1, inplace=True)

    # print(df)
    # exit()

    if int(hour) > 10:
        df.to_excel('C:\\Users\Administrator\Desktop\现金贷催收{}月{}日报告.xlsx'.format(yue, ri_now), index=False)
    else:
        df.to_excel('C:\\Users\Administrator\Desktop\现金贷催收{}月{}日报告.xlsx'.format(yue, ri), index=False)
    print('\n没有问题，统计已存放桌面！')

