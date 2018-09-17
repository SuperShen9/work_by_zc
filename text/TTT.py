# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import numpy as np

df = pd.read_hdf('D:\Super\database\\before9\data0831.h5', key='data')

print('\n9月之前数据量：{}'.format(df.shape[0]))

df2 = pd.read_hdf('D:\Super\database\data.h5', key='data')

print('\n9月之后数据量：{}'.format(df2.shape[0]))