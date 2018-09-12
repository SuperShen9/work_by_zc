# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import os
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

# 接收文件路径
path = 'C:\\Users\\Administrator\\Documents\\WeChat Files\\shenyuanji9339\\Files\\fast.xlsx'
# 判断是否存在接收文件
if os.path.isfile(path):
    print('\n存在接收文件，请知悉！')
    df_dup = pd.read_excel(path)
else:
    print('\n数据从原始文件中提取！')
    df_dup = pd.read_excel('D:\Super\dapeng\\fast.xlsx')

# 读取去重数据
df = pd.read_hdf('D:\Super\dapeng\data_sd_dup.h5', key='data')

# print('赎当数据量：{}'.format(df.shape[0]))
# exit()

# 读取去重数据2
df_huan = pd.read_excel('D:\Super\dapeng\\渠道A {}10.xlsx'.format(yue, ri))

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
df.to_excel('C:\\Users\Administrator\Desktop\\渠道A去重.xlsx', index=False)

# 删除-接收文件
os.remove(path)
print('\n原始文件已删除！')



# # 数据第一次存贮
# df = pd.read_excel('D:\Super\dapeng\\0814tonow.xlsx')
# df1 = pd.read_excel('D:\Super\dapeng\\oldto0813.xlsx')
# df = df.append(df1, ignore_index=True)
# df.to_hdf('D:\Super\dapeng\data_sd_dup.h5', key='data')



# # series方法代码
# print(list(df.head().groupby('手机号').size().index))
# print(df.head().groupby('手机号').size().values)

