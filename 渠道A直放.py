# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
from Func import nian, yue, ri_now, ri

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

# 第二次：去重再保存
# df = pd.read_hdf('D:\Super\dapeng\data_sd_dup.h5', key='data')
# no1 = df.shape[0]
# df1 = pd.read_excel('D:\Super\dapeng\\1\\ADD09{}.xlsx'.format(ri_now))
# df = df.append(df1, ignore_index=True)
# df = df.drop_duplicates(subset=['借款订单号'], keep='last')
# no2 = df.shape[0]
# print('data add：{}'.format(no2-no1))
# df.to_hdf('D:\Super\dapeng\data_sd_dup.h5', key='data')
# exit()

df = pd.read_hdf('D:\Super\dapeng\data_sd_dup.h5', key='data')

df_dup = pd.read_excel('D:\Super\dapeng\\fast.xlsx')

df_huan = pd.read_excel('D:\Super\dapeng\\渠道A {}{}.xlsx'.format(yue, ri))
df_huan = df_huan[['手机号', '借款状态']]

df1 = df.groupby('手机号').size()

df1 = df1.reset_index()

df = pd.merge(left=df_dup, right=df1, on='手机号', how='left')
df = pd.merge(left=df, right=df_huan, on='手机号', how='left')

cdt1 = df[0].notnull()
cdt2 = df['借款状态'].notnull()

df.loc[cdt1 & cdt2, 'Flag'] = '1, 申请过借款且在还款中'

df.to_excel('C:\\Users\Administrator\Desktop\\渠道A去重.xlsx', index=False)












# # 数据第一次存贮
# df = pd.read_excel('D:\Super\dapeng\\0814tonow.xlsx')
# df1 = pd.read_excel('D:\Super\dapeng\\oldto0813.xlsx')
# df = df.append(df1, ignore_index=True)
# df.to_hdf('D:\Super\dapeng\data_sd_dup.h5', key='data')



# # series方法代码
# print(list(df.head().groupby('手机号').size().index))
# print(df.head().groupby('手机号').size().values)

