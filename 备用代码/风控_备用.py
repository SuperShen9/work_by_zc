# -*- coding: utf-8 -*-
# author：Super.Shen

import os, openpyxl
import pandas as pd
from Daily.Func import yue,ri
os.chdir('D:\Super\superflag')

wbf = openpyxl.load_workbook('数据合并.xlsx')

sheet = wbf['审核']

hang1 = sheet.max_row + 1

spam = {}
for row in range(2, hang1):
    flag = sheet['A' + str(row)].value.lower()
    number = sheet['B' + str(row)].value
    spam.setdefault(flag, number)

filepath = 'D:\Super\\tongji_hebing'

os.chdir(filepath)
df = pd.DataFrame()

for x, y, excels in os.walk(filepath):
    len_fk = len(excels)
    for excel in excels:
        df1 = pd.read_excel(excel)
        df = df.append(df1)

df = df.reset_index(drop=True)

# 筛选出不属于昨天的数据
df = df[df['审核员姓名'] != '张三']
# try:
#     df = df[df['日期'] >= pd.to_datetime('{}-{}-{}'.format(nian, yue, ri))]
# except TypeError:
#     print('请核对数据日期格式')
#     exit()
#
# print('风控统计人数：{}'.format(len_fk))



# if df.shape[0] != len_fk:
#     df.to_excel('C:\\Users\Administrator\Desktop\风控部门核对.xlsx', index=False)
#     print('数据数量有问题，请核对!')
#     exit()
# else:
#     df.loc[len_fk + 1, '审核员姓名'] = '风控汇总'
#     for col in df.columns[2:]:
#         pass
        # df.loc[len_fk + 1, col] = df[col].sum()

df.to_excel('C:\\Users\Administrator\Desktop\风控部门{}月{}日报告.xlsx'.format(yue,ri), index=False)