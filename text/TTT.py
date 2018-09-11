# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import numpy as np

s5 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s6 = pd.Series([2, 3, 4], index=['b', 'c', 'd'])

print(pd.concat([s5, s6], axis=1, sort=True, join='outer', keys=['one', 'two']))