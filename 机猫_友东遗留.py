# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
from Daily import Func
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

df = pd.read_excel('D:\Super\shudang\友东_遗留数据.xlsx')

df_dup = pd.read_excel('D:\Super\shudang\每日核对数据.xlsx')

no1 = df.shape[0]
no2 = df_dup.shape[0]

df_dup = df_dup[['手机号', '数据反馈']]
df_dup['手机号'].apply(lambda x: int(x))

df = pd.merge(left=df, right=df_dup, on='手机号', how='left')
df = df[df['数据反馈'].isnull()]
df = df.drop_duplicates(subset=['手机号'], keep='last')
df=df.reset_index(drop=True)
print('\n数据数量统计：{}'.format(df.shape[0]))

df.to_excel('C:\\Users\Administrator\Desktop\友东_{}{}遗留数据.xlsx'.format(Func.yue,Func.ri_now))


