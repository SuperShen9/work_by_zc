# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import os

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

# 接收文件路径
path = 'C:\\Users\Administrator\Desktop\dapeng\\fast.xlsx'
# 判断是否存在接收文件
if os.path.isfile(path):
    print('\n存在接收文件，请知悉！')
    df_dup = pd.read_excel(path)
else:
    print('\n数据不存在！')
    exit()

# 读取去重数据
df = pd.read_hdf('C:\\Users\Administrator\Desktop\dapeng\data_sd_dup.h5', key='data')

# 读取去重数据2
df_huan = pd.read_hdf('C:\\Users\Administrator\Desktop\dapeng\\0913.h5', key='huan')

# 提取需求标签
df_huan = df_huan[['手机号', '借款状态']]

# 提取号码次数
df1 = df.groupby('手机号').size()

# 重置索引
df1 = df1.reset_index()

# 合并2个表
df = pd.merge(left=df_dup, right=df1, on='手机号', how='left')
df = pd.merge(left=df, right=df_huan, on='手机号', how='left')
# 筛选条件
cdt1 = df[0].notnull()
cdt2 = df['借款状态'].notnull()

# 填入符合条件的值
df.loc[cdt1 & cdt2, 'Flag'] = '1, 申请过借款且在还款中'

# 重命名列名
df.rename(columns={0: '还款次数'}, inplace=True)

# 导出数据
df.to_excel('C:\\Users\Administrator\Desktop\\去重结果.xlsx', index=False)

exit()
# 删除-接收文件
os.remove(path)
print('\n原始文件已删除！')


