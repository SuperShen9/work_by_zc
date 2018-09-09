# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
from Func import ri_now
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

df = pd.read_excel('D:\Super\\xianjindai\当日到期.xlsx')
df['续期时间'] = df['应还时间'].apply(lambda x: x[8:10])

df.loc[df['续期时间'] != str(ri_now), '订单状态'] = '已续期'
# df.loc[df['续期时间'] != '08', '订单状态'] = '已续期'
# df.loc[df['续期时间'] == '16', '订单状态'] = '已逾期'


df_name = pd.read_excel('D:\Super\\xianjindai\审核员.xlsx')
df = pd.merge(left=df, right=df_name, on='审核员', how='left')

df_sec = pd.read_excel('D:\Super\\xianjindai\\2表复制.xlsx')

# df.to_excel('C:\\Users\Administrator\Desktop\\核对.xlsx')
# print(df.head())
# exit()

# 第一个表的程序
df1 = pd.DataFrame()
df1.loc[0, '到期总数'] = df.shape[0]
df1.loc[0, '新单到期'] = df[df['新老单'] == '新客户'].shape[0]
df1.loc[0, '老单到期'] = df[df['新老单'] == '老客户'].shape[0]
df1.loc[0, '续期客户'] = df[df['订单状态'] == '已续期'].shape[0]
df1.loc[0, '已完结'] = df[df['订单状态'] == '已完结'].shape[0]
df1.loc[0, 'kong1'] = ''
df1.loc[0, 'kong2'] = ''

# df.to_excel('C:\\Users\Administrator\Desktop\现金贷第一个表.xlsx', index=False)
# exit()

df1.loc[0, '新单逾期'] = df[df['订单状态'] == '待付租'][df['新老单'] == '新客户'].shape[0]
df1.loc[0, '老单逾期'] = df[df['订单状态'] == '待付租'][df['新老单'] == '老客户'].shape[0]

df1.to_excel('C:\\Users\Administrator\Desktop\现金贷第一个表.xlsx', index=False)

# 第二个表程序
df2 = pd.DataFrame()

ii = 0
for x, y in df.groupby('标准名字'):
    y = y.reset_index(drop=True)
    df2.loc[ii, '姓名'] = x

    y_new = y[y['新老单'] == '新客户']
    df2.loc[ii, '到期新单'] = y_new.shape[0]
    df2.loc[ii, '逾期新单'] = y_new[y['订单状态'] == '待付租'].shape[0]
    df2.loc[ii, '到期新单金额'] = y_new['回租价格'].sum()-y_new['日租金'].sum()

    y_old = y[y['新老单'] == '老客户']
    df2.loc[ii, '到期老单'] = y_old.shape[0]
    df2.loc[ii, '逾期老单'] = y_old[y['订单状态'] == '待付租'].shape[0]
    df2.loc[ii, '到期老单金额'] = y_old['回租价格'].sum() - y_old['日租金'].sum()

    ii += 1

df2 = pd.merge(left=df_sec, right=df2, on='姓名', how='left')
df2.fillna(value=0, inplace=True)
df2.to_excel('C:\\Users\Administrator\Desktop\现金贷SEC表.xlsx', index=False)


