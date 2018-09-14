# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2, 2, 2, 2],
                   'B': [3, 3, 4, 4, 4],
                   'C': [1, 1, np.nan, 1, 1]})
print(df)
print('-----')

print(pd.crosstab(df['A'], df['B']))
print('-----')