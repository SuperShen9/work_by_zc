# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
from pyecharts import Line
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

df = pd.read_excel('C:\\Users\Administrator\Desktop\dianxiao_Data.xlsx')
df['day'] = df['日期'].apply(lambda x:str(x).split('-')[-1][:2])
df = df[['day', '电销姓名', '成交客户']]

# # 筛选人数
# cdt1 = df['电销姓名'] == '张加胜'
# # cdt2 = df['电销姓名'] == '张嘉庆'
# cdt3 = df['电销姓名'] == '欧阳小蝶'
# df = df[cdt1 | cdt3]
# # df = df[cdt1 | cdt2 | cdt3]

df = df.reset_index(drop=True)

att = df['day'].drop_duplicates().to_frame()
heng = df['day'].drop_duplicates().drop_duplicates().sort_values().tolist()

list_all = []
list_name = []

count=0
for x, y in df.groupby('电销姓名'):
    y = pd.merge(left=att,right=y,on='day',how='left')
    y['成交客户'].fillna(value=0.0, inplace=True)
    y.sort_values(by='day', inplace=True)
    list_name.append(x)
    list_all.append(y['成交客户'].tolist())
    count += 1

name='7月电销'
line = Line(name)

for x in range(len(list_name)):
    line.add(list_name[x], heng, list_all[x], is_smooth=True)

line.show_config()
line.render("%s.html" %name)
