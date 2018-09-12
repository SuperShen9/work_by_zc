# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(20).reshape(5, 4),
                  columns=['a', 'b1', 'c', 'd23'])

print(df)

print('-'*50)

print(df.groupby(len, axis=1).sum())