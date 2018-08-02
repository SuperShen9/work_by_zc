# -*- coding: utf-8 -*-
# author：Super.Shen
import pandas as pd
import os
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

# df = pd.read_excel('C:\\Users\Administrator\Desktop\所有已赎当数据\\已赎当 7月之前.xlsx')
# df1 = pd.read_excel('C:\\Users\Administrator\Desktop\所有已赎当数据\\已赎当 0701-0714.xlsx')
# df2 = pd.read_excel('C:\\Users\Administrator\Desktop\所有已赎当数据\\已赎当 0715-0801.xlsx')
#
# df = df.append(df1, ignore_index=True)
# df = df.append(df2, ignore_index=True)
#
# df.to_hdf('C:\\Users\Administrator\Desktop\shudang\\shudang.h5', key='shudang', mode='w')

df = pd.read_hdf('D:\Super\shudang\\shudang.h5', key='shudang')

df_dup = pd.read_excel('D:\Super\shudang\每日核对数据.xlsx')



print(df_dup)