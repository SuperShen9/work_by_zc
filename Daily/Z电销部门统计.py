# -*- coding: utf-8 -*-
# author：Super.Shen

import os, openpyxl
import pandas as pd
from Func import file_arrange

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

from Daily.Func import nian,yue,ri_now
if len(yue) < 2:
    yue = '0' + yue
if len(ri_now) < 2:
    ri_now = '0' + ri_now

os.chdir('D:\Super\superflag')

wbf = openpyxl.load_workbook('数据合并.xlsx')

sheet = wbf['电销部门每日报告']

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
        df = df.append(df1)
        list1.append(excel.split('-')[1])

print('\n电销统计人数：{}'.format(len_dx))

# 筛选出不属于昨天的数据
df = df[df['电销姓名'] != '张三']
df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri_now))]
# df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, '21'))]

df = df.reset_index(drop=True)

i = 20
if df.shape[0] != len_dx:
    error = [l for l in list1 if l not in list(df['电销姓名'])]
    print('\n{} 的日期有问题，请核对!'.format(error))

else:
    # df.to_excel('C:\\Users\Administrator\Desktop\电销-{}{}-上传.xlsx'.format(yue, ri_now),index=False)

    df.loc[len_dx+i, '电销姓名'] = '电销汇总'
    df.loc[len_dx + i + 1, '日期'] = ''
    df.loc[len_dx + i + 2, '日期'] = ''
    df.loc[len_dx + i + 3, '日期'] = 'Flag'
    df.loc[len_dx + i + 3, '电销姓名'] = '电销汇总'
    k = 4
    for col in df.columns[2:]:
        df.loc[len_dx + i, col] = df[col].sum()
        df.loc[len_dx + i + k, '日期'] = col
        df.loc[len_dx + i + k, '电销姓名'] = df.loc[len_dx + i, col]
        k += 1

    df['提交率'] = df['提交客户']/df['已打资源']
    df['成交率'] = df['成交客户']/df['已打资源']

    df.loc[len_dx + i + 30, '电销姓名'] = df.loc[len_dx + i, '提交率']
    df.loc[len_dx + i + 30, '日期'] = '提交率'
    df.loc[len_dx + i + 31, '电销姓名'] = df.loc[len_dx + i, '成交率']
    df.loc[len_dx + i + 31, '日期'] = '成交率'

    df.to_excel('C:\\Users\Administrator\Desktop\电销部门{}月{}日报告.xlsx'.format(yue, ri_now), index=False)
    print('\n没有问题，统计已存放桌面！')


