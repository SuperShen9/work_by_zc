# -*- coding: utf-8 -*-
# author：Super.Shen

import os, openpyxl
import pandas as pd
import datetime
hour = datetime.datetime.now().strftime('%H')

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

from Daily.Func import yue,ri_now,ri
if len(yue) < 2:
    yue = '0' + yue
if len(ri_now) < 2:
    ri_now = '0' + ri_now
if len(ri) < 2:
    ri = '0' + ri


os.chdir('D:\Super\superflag')

wbf = openpyxl.load_workbook('数据合并.xlsx')

sheet = wbf['审核资料统计']

hang1 = sheet.max_row + 1

spam = {}
for row in range(2, hang1):
    flag = sheet['A' + str(row)].value.lower()
    number = sheet['B' + str(row)].value
    spam.setdefault(flag, number)

filepath = 'D:\Super\每日报告合并'

os.chdir(filepath)
df = pd.DataFrame()

list1 = []
for x, y, excels in os.walk(filepath):
    len_dx = len(excels)
    for excel in excels:
        df1 = pd.read_excel(excel)
        df1[['日期','审核员姓名']] = df1[['日期','审核员姓名']].fillna(method='ffill')
        df = df.append(df1)
        list1.append(excel.split('-')[1])

df = df[['日期','审核员姓名','资料姓名','资料手机号','收集情况']]

print('\n资料收集统计人数：{}\n'.format(len_dx))

# 筛选出不属于昨天的数据
if int(hour) > 11:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri_now))]
else:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri))]
    # df = df[df['日期'] == pd.to_datetime('20180810')]

df = df.reset_index(drop=True)

i = 20
if df['审核员姓名'].drop_duplicates().count() != len_dx:
    error = [l for l in list1 if l not in list(df['审核员姓名'])]
    print('\n{} 的日期有问题，请核对!'.format(error))

else:
    df_add = pd.DataFrame(df.groupby('收集情况').size())

    # 提取原始index；重命名【列】
    df_add.reset_index(inplace=True)
    df_add.columns = ['收集情况', '数量']
    # 按照数量进行排序
    df_add.sort_values(by='数量', ascending=0, inplace=True)
    # 重置索引
    df_add = df_add.reset_index(drop=True)
    # 计算百分比
    df_add['百分比'] = df_add['数量']/df.shape[0]

    df.loc[1, ' '] = ' '
    df = pd.concat([df, df_add], axis=1)

    if int(hour) > 11:
        df.to_excel('C:\\Users\Administrator\Desktop\审核资料{}月{}日统计.xlsx'.format(yue, ri_now), index=False)
    else:
        df.to_excel('C:\\Users\Administrator\Desktop\审核资料{}月{}日统计.xlsx'.format(yue, ri), index=False)

    print('\n没有问题，统计已存放桌面！')


