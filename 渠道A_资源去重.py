# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

df = pd.read_hdf('D:\Super\database\data.h5', key='data')
print(df.shape[0])
exit()

df_dup = pd.read_excel('D:\Super\dapeng\\yuqi0907.xlsx')

df_dup['flag'] = 'yuqi'

df_dup = df_dup[['手机号', 'flag']]

df = pd.merge(left=df, right=df_dup, on=['手机号'], how='left')

print(df.head())