# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import numpy as np
import datetime
s1 = pd.Series([1,2,3])
s2 = pd.Series([2,3,4])
s3 = pd.Series([1,2,3],index = ['a','c','h'])
s4 = pd.Series([2,3,4],index = ['b','e','d'])

print(s1.isin(s4))