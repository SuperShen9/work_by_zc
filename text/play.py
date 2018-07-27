# -*- coding: utf-8 -*-
# author：Super.Shen
import os
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1500)

df = pd.read_excel('C:\\Users\Administrator\Desktop\play\\借款订单20180717.xlsx')
print(df)

df = df.reset_index(drop=True)
print(df)


