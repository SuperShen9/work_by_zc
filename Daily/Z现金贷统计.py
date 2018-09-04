# -*- coding: utf-8 -*-
# author：Super.Shen

import os, openpyxl
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
df = df[df['姓名'] != '张三1']

if int(hour) > 10:
    # df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri_now))]
    df = df[df['日期'] == pd.to_datetime('20180903')]
else:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri))]
    # df = df[df['日期'] == pd.to_datetime('20180804')]

# df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue,'16'))]

df = df.reset_index(drop=True)

df.sort_values(by='阶段', inplace=True)

i = 20
if df.shape[0] != len_cs:
    error = [l for l in list1 if l not in list(df['姓名'])]
    print('\n{} 的日期有问题，请核对!'.format(error))

else:
    df['阶段'] = df['阶段'].apply(lambda x: x.upper())
    df.sort_values(by='阶段', inplace=True)
    df.loc[len_cs + i, '阶段'] = '汇总:'
    df.loc[len_cs + i, '姓名'] = df['姓名'].count()

    df = df[['日期','阶段','姓名','分单量','停机','关机','空号','设置','未接','拒接','接通单数','总持单量','完结','续期','部分还款','部分还款金额','代扣金额','催回率','催回总金额']]

    for col in df.columns[3:]:
        df.loc[len_cs + i, col] = df[col].sum()

    df['催回率'] = (df['完结'] + df['续期'])/df['分单量']

    # print(df)
    # exit()

    if int(hour) > 10:
        df.to_excel('C:\\Users\Administrator\Desktop\现金贷催收{}月{}日报告.xlsx'.format(yue, ri_now), index=False)
    else:
        df.to_excel('C:\\Users\Administrator\Desktop\现金贷催收{}月{}日报告.xlsx'.format(yue, ri), index=False)
    print('\n没有问题，统计已存放桌面！')



    # # 8月底 - 何远开 第一次更新
    # df['新单催回率'] = df['新单催回量'] / df['新单量']
    # df['总催回率'] = (df['新单催回量'] + df['老单回款量'] + df['部分还款量']) / df['总持单量']
    #
    # df.loc[len_cs + i + 1, '阶段'] = '新单到期'
    # df.loc[len_cs + i + 1, '姓名'] = df[df['阶段'] == 's1']['新单量'].sum()
    #
    # df.loc[len_cs + i + 1, '新单量'] = '新单处理'
    # df.loc[len_cs + i + 1, '总持单量'] = df[df['阶段'] == 's1']['新单催回量'].sum()
    #
    # df.loc[len_cs + i + 1, '新单催回量'] = 's1新单催回率'
    # df.loc[len_cs + i + 1, '老单回款量'] = df.loc[len_cs + i + 1, '总持单量'] / df.loc[len_cs + i + 1, '姓名']


    # # df.to_excel('C:\\Users\Administrator\Desktop\催收-{}{}-上传.xlsx'.format(yue, ri_now), index=False)
    #
    # df.loc[len_cs+i, '姓名'] = '现金贷催收汇总'
    #
    # # 汇总标签
    # df.loc[len_cs + i + 1, '日期'] = ''
    # df.loc[len_cs + i + 2, '日期'] = ''
    # df.loc[len_cs + i + 3, '日期'] = 'Flag'
    # df.loc[len_cs + i + 3, '姓名'] = '现金贷催收汇总'
    #
    #
    # k = 4
    # for col in df.columns[3:]:
    #     if col == '回款率':
    #         df.loc[len_cs + i, col]= (df.loc[len_cs + i, '催回全款笔数']+df.loc[len_cs + i, '催回续期笔数'])/df.loc[len_cs + i, '逾期笔数']
    #         df.loc[len_cs + i + k, '日期'] = col
    #         df.loc[len_cs + i + k, '姓名'] = df.loc[len_cs + i, col]
    #     else:
    #         df.loc[len_cs+i, col] = df[col].sum()
    #         df.loc[len_cs + i + k, '日期'] = col
    #         df.loc[len_cs + i + k, '姓名'] = df.loc[len_cs+i, col]
    #
    #     k += 1