# -*- coding: utf-8 -*-
# author：Super.Shen

import os, openpyxl
import pandas as pd
from Daily.Func import yue, ri,ri_now
import datetime
hour = datetime.datetime.now().strftime('%H')
if len(yue) < 2:
    yue = '0' + yue
if len(ri_now) < 2:
    ri_now = '0' + ri_now
if len(ri) < 2:
    ri = '0' + ri

os.chdir('D:\Super\superflag')

wbf = openpyxl.load_workbook('数据合并.xlsx')

sheet = wbf['现金贷催收']

hang1 = sheet.max_row + 1

spam = {}
for row in range(2, hang1):
    flag = sheet['A' + str(row)].value.lower()
    number = sheet['B' + str(row)].value
    spam.setdefault(flag, number)

filepath = 'D:\Super\\每日报告合并'

os.chdir(filepath)
df = pd.DataFrame()

list1 = []
for x, y, excels in os.walk(filepath):
    len_cs = len(excels)
    for excel in excels:
        df1 = pd.read_excel(excel)
        df = df.append(df1)
        list1.append(excel.split('-')[1])

print('\n现金贷催收统计人数：{}'.format(len_cs))

# 筛选出不属于昨天的数据
df = df[df['姓名'] != '张三']

if int(hour) > 10:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri_now))]
    # df = df[df['日期'] == pd.to_datetime('20180805')]
else:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri))]
    # df = df[df['日期'] == pd.to_datetime('20180804')]

# df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue,'16'))]

df = df.reset_index(drop=True)

i = 20
if df.shape[0] != len_cs:
    error = [l for l in list1 if l not in list(df['姓名'])]
    print('\n{} 的日期有问题，请核对!'.format(error))

else:

    # df.to_excel('C:\\Users\Administrator\Desktop\催收-{}{}-上传.xlsx'.format(yue, ri_now), index=False)

    df.loc[len_cs+i, '姓名'] = '现金贷催收汇总'

    # 汇总标签
    df.loc[len_cs + i + 1, '日期'] = ''
    df.loc[len_cs + i + 2, '日期'] = ''
    df.loc[len_cs + i + 3, '日期'] = 'Flag'
    df.loc[len_cs + i + 3, '姓名'] = '现金贷催收汇总'


    k = 4
    for col in df.columns[2:]:
        if col == '回款率':
            df.loc[len_cs + i, col]= (df.loc[len_cs + i, '催回全款笔数']+df.loc[len_cs + i, '催回续期笔数'])/df.loc[len_cs + i, '逾期笔数']
            df.loc[len_cs + i + k, '日期'] = col
            df.loc[len_cs + i + k, '姓名'] = df.loc[len_cs + i, col]
        else:
            df.loc[len_cs+i, col] = df[col].sum()
            df.loc[len_cs + i + k, '日期'] = col
            df.loc[len_cs + i + k, '姓名'] = df.loc[len_cs+i, col]

        k += 1

    if int(hour) > 10:
        df.to_excel('C:\\Users\Administrator\Desktop\现金贷催收{}月{}日报告.xlsx'.format(yue, ri_now), index=False)
    else:
        df.to_excel('C:\\Users\Administrator\Desktop\现金贷催收{}月{}日报告.xlsx'.format(yue, ri), index=False)
    print('\n没有问题，统计已存放桌面！')