# -*- coding: utf-8 -*-
# author：Super.Shen
import pandas as pd
import os
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

# file = 'C:\\Users\Administrator\Desktop\play\借款订单20180717.xlsx'
# file1 = 'C:\\Users\Administrator\Desktop\play\A.xlsx'
# file2 = 'C:\\Users\Administrator\Desktop\play\B.xlsx'
#
# df = pd.read_excel(file)
# df1 = pd.read_excel(file1)
# df2 = pd.read_excel(file2)

# df.to_hdf('C:\\Users\Administrator\Desktop\play\\all.h5',key='all')
# df1.to_hdf('C:\\Users\Administrator\Desktop\play\\first.h5',key='f')
# df2.to_hdf('C:\\Users\Administrator\Desktop\play\\second.h5',key='s')

df = pd.read_hdf('C:\\Users\Administrator\Desktop\play\\all.h5',key='all')
# df1 = pd.read_hdf('C:\\Users\Administrator\Desktop\play\\first.h5',key='f')
# df2 = pd.read_hdf('C:\\Users\Administrator\Desktop\play\\second.h5',key='s')
df['date'] = df['申请典当时间'].apply(lambda x: pd.to_datetime(x[:10]))
df1 =df[df['date']>=pd.to_datetime('2018-07-11')]
# print(df1)
# exit()
print(df.groupby('date').size())
print(df.groupby('date').size().sum())
print('-'*25)
# print(df1.groupby('date').size())
print(df1.groupby('date').size().sum())
exit()

# df['Flag']='a'
# df1['Flag']='b'
# # print(df.head())
#
# no1=df.shape[0]
# no2=df1.shape[0]
#
# df = df.append(df1, ignore_index=False, sort=True)
#
# df.drop_duplicates(subset=['借款订单号'], keep='first', inplace=True)
#
# print(df[df['Flag']=='b'])
# print(df[df['Flag']=='b'].shape[0])