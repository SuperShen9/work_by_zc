# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)  # 显示1000行


df = pd.read_excel('C:\\Users\Administrator\Desktop\pandas0824\\现金贷_数据推算.xlsx')

print(df)