# -*- coding: utf-8 -*-
# author：Super.Shen

import os
import pandas as pd
import datetime
hour = datetime.datetime.now().strftime('%H')

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

from Func import ri_zhou, yue, ri_now, ri
if len(yue) < 2:
    yue = '0' + yue
if len(ri_now) < 2:
    ri_now = '0' + ri_now
if len(ri) < 2:
    ri = '0' + ri
if len(ri_zhou) < 2:
    ri_zhou = '0' + ri_zhou


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

print('\n陈磊周报统计人数：{}\n'.format(len_dx))

# 筛选出不属于昨天的数据
df = df[df['审核姓名'] != '张三']
if int(hour) > 11:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri_now))]
else:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri))]

df = df.reset_index(drop=True)


i = 20
if df.shape[0] != len_dx:
    error = [l for l in list1 if l not in list(df['审核姓名'])]
    print(list(df['审核姓名']))
    print('\n{} 的日期有问题，请核对!'.format(error))

else:
    df.loc[len_dx+i, '审核姓名'] = '总计'

    for col in df.columns[2:]:
        df.loc[len_dx + i, col] = df[col].sum()

    df = df[df.columns[1:]]

    df.to_excel('C:\\Users\Administrator\Desktop\{}月{}号 - {}月{}号周报.xlsx'.format(yue, ri_zhou, yue, ri_now), index=False)
    print('\n没有问题，统计已存放桌面！')


