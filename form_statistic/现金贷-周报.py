# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import os
from Func import ri_now
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

filepath = 'D:\Super\每日报告合并'

os.chdir(filepath)
df = pd.DataFrame()

list1 = []
for x, y, excels in os.walk(filepath):
    for excel in excels:
        df1 = pd.read_excel(excel, skiprows=1)
        df = df.append(df1)

# df.dropna(how='all', inplace=True)

# 清除空列
df = df[df['姓名'].notnull()]
df = df[df['姓名'] != '汇总']

# 补充缺失值
df.fillna(value=0, inplace=True)

# 透视汇总
df = df.groupby('姓名').sum()
df.reset_index(inplace=True)

# 计算表宽
len_cs = df.shape[0]+1

# 添加汇总列
df.loc[len_cs, '姓名'] = '汇总'
# 汇总列求和
for col in df.columns[1:]:
    df.loc[len_cs, col] = df[col].sum()

# 重置各种累计的比例
df['新单转化率'] = df['通过']/df['申请单量']
df['首逾新单'] = df['逾期新单']/df['到期新单']
df['首逾老单'] = df['逾期老单']/df['到期老单']
df['综合首逾'] = (df['逾期新单']+df['逾期老单'])/(df['到期新单']+df['到期老单'])

# 填充为0的单元格
df.fillna(value=0, inplace=True)

# print(df)
# exit()
# 导出数据
df.to_excel('C:\\Users\Administrator\Desktop\现金贷-审核 -第二周.xlsx', index=False)

# # 画图操作
# from pyecharts import Line
#
# # print(list(df['新单转化率']))
# # exit()
#
# attr = list(df['姓名'])
# v1 = list(df['新单转化率'])
# v2 = list(df['首逾新单'])
# v3 = list(df['首逾老单'])
# v4 = list(df['综合首逾'])
#
# line = Line("现金贷-审核")
# line.add("新单转化", attr, v1, mark_point=["average"])
# line.add("首逾新单", attr, v2, is_smooth=True)
# line.add("首逾老单", attr, v3, is_smooth=True)
# line.add("综合首逾", attr, v4, is_smooth=True)
# line.show_config()
# line.render()
