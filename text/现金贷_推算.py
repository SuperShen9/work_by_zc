# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)  # 显示1000行

df = pd.DataFrame()
# 总金额
all_cash = 10000000
# 放款天数
day = 15
# 每天放款单数
count = all_cash/day
# 还款利率
lixi = 250/750

# 新单参数比例
yuqi = 0.25 #新单逾期率
huankuan = 0.3  #新单还款率
xuqi = 1-yuqi-huankuan  #新单续期率

# 老单参数比例
yuqi2 = 0.2 #老单逾期率
huankuan2 = 0.3 #老单还款率
xuqi2 = 1-yuqi-huankuan #老单续期率





















