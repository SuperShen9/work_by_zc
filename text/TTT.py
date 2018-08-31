# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import numpy as np
import datetime
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)  # 显示1000行

t1 = pd.to_datetime('2017-12-21')
print('\n')
print(t1, type(t1))