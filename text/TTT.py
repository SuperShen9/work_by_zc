# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import numpy as np

df = pd.read_excel('C:\\Users\\Administrator\\Desktop\\中午逾期统计\\放款逾期统计表(2).xlsx')


# 画图操作
from pyecharts import Line

attr = list(df['日期'].apply(lambda x:str(x)))
v1 = list(df['首逾'])
v2 = list(df['新单首逾'])
v3 = list(df['老单首逾'])
v4 = list(df['目前逾期率'])

line = Line("现金贷-审核")
line.add("首逾", attr, v1, mark_point=["average"])
line.add("新单首逾", attr, v2, is_smooth=True)
line.add("老单首逾", attr, v3, is_smooth=True)
line.add("目前逾期率", attr, v4, is_smooth=True)
line.show_config()
line.render('C:\\Users\\Administrator\\Desktop\\中午逾期统计\\text.html')