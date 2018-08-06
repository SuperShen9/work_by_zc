# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import os
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

df = pd.read_hdf('D:\Super\shudang\\shudang.h5', key='shudang')

df_dup = pd.read_excel('D:\Super\shudang\每日核对数据.xlsx')

no1 = df.shape[0]

df_dup = df_dup[['手机号','数据反馈']]
df_dup['手机号'].apply(lambda x: int(x))


df =pd.merge(left=df,right=df_dup,on='手机号',how='left')
df = df[df['数据反馈'].isnull()]
no2 = df.shape[0]
df['日期'] = df['申请典当时间'].apply(lambda x: x[:10])
df['排序'] = df['申请典当时间'].apply(lambda x: x[14:16])

df = df.drop_duplicates(subset=['手机号'], keep='first')
no3 = df.shape[0]

print('\n去重数据量：{}'.format(no2-no3))

df.to_excel('C:\\Users\Administrator\Desktop\机猫赎当_当日去重.xlsx', index=False)

