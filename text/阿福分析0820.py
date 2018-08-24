# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000) #显示1000行

# df = pd.read_hdf('C:\\Users\Administrator\Desktop\panda0820\pandas.h5')
df = pd.read_excel('C:\\Users\Administrator\Desktop\panda0820\\file.xlsx')
# df = df.drop_duplicates(subset=['tel'], keep='first')
# print(df.groupby('Flag').size())

# # 求出每个人每次申请金额的平均值
df['min'] = df['loanAmount'].apply(lambda x: x[1: -1].split(',')[0])
df['max'] = df['loanAmount'].apply(lambda x: x[1: -1].split(',')[1].replace('+','0'))
df['ave'] = (df['min'].apply(lambda x: int(x))+df['max'].apply(lambda x: int(x)))/2

# print(df.head(20))
# exit()
# # 每个电话的总申请量
series1 = df.groupby('tel').size()
series2 = df.groupby('tel')['periods'].mean()
series3 = df.groupby('tel')['ave'].mean()

series4 = df[df['shenpi'] == 1].groupby('tel')['shenpi'].size()
series5 = df[df['shenpi'] == 0].groupby('tel')['shenpi'].size()

series10 = df.groupby('tel')['Flag'].first()

df1 = pd.DataFrame([series1, series2, series3, series4, series5, series10]).T
df1.reset_index(inplace=True)
df1.columns = ['Tel', 'size', 'periods', 'ave_cash', 'shenpi_1', 'shenpi_0','Flag']
df1.fillna(value=0, inplace=True)

df1.to_hdf('C:\\Users\Administrator\Desktop\panda0820\\file.h5', key='data')

