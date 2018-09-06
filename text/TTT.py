# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import numpy as np
import datetime
# 修补 pd.combine_first()

df1 = pd.DataFrame([[np.nan, 3., 5.], [-4.6, np.nan, np.nan],[np.nan, 7., np.nan]])
df2 = pd.DataFrame([[-42.6, np.nan, -8.2], [-5., 1.6, 4]],index=[1, 2])
print(df1)
print('-'*50)
print(df2)
print('-'*50)
print(df1.combine_first(df2))
print('-'*50)
# 根据index，df1的空值被df2替代
# 如果df2的index多于df1，则更新到df1上，比如index=['a',1]

df1.update(df2)
print(df1)
# update，直接df2覆盖df1，相同index位置