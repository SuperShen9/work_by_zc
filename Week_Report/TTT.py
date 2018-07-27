# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1500)
path = 'C:\\Users\Administrator\Desktop\风控部门错误标记-周.xlsx'
df=pd.read_excel(path)
df=df[df.columns[1:]]
print(df)

