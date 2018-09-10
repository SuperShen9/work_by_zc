# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
from Func import yue, ri
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

# 读取总数据
df = pd.read_hdf('D:\Super\database\data.h5', key='data')
# 读取当日数据
# df_dup = pd.read_excel('C:\\Users\Administrator\Desktop\渠道A{}{}.xlsx'.format(yue, ri))

df_dup = pd.read_excel('C:\\Users\Administrator\Desktop\渠道A0907.xlsx'.format(yue, ri))

# 标记总数据为打过
df['Flag'] = 'call'
# 提取总数据指定的2列
df = df[['手机号', 'Flag']]
# 合并2个表
df = pd.merge(left=df_dup, right=df, on=['手机号'], how='left')

# 去重数据
df = df[df['Flag'].isnull()]

# 根据时间打乱数据
df['Flag'] = df['申请典当时间'].apply(lambda x: x[18:])
df.sort_values(by='Flag', inplace=True)

# 重置index，并引申为列
df = df.reset_index(drop=True)
df.reset_index(inplace=True)

# 序列号+1
df['index'] = df['index'].apply(lambda x: x+1)

# 取出有效索引
df = df[['index', '用户姓名', '手机号', '申请典当时间']]

df.to_excel('C:\\Users\Administrator\Desktop\渠道A{}{}_run.xlsx'.format(yue,ri), index=False)
exit()
print(df.head())