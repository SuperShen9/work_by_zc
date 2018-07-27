# -*- coding: utf-8 -*-
# author：Super.Shen
import pandas as pd
import os
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

file1='C:\\Users\Administrator\Desktop\Feedback_Data.xlsx'
file2='C:\\Users\Administrator\Desktop\Week_Data.xlsx'

list1 = [file1, file2]

for no, i in enumerate(list1):
    if os.path.exists(i):
        df = pd.read_excel(i)

        # 统计接通率/需求率
        i = 0
        df1 = pd.DataFrame()
        for x, y in df.groupby(['资源来源']):
            df1.loc[i, '资源名称'] = x
            df1.loc[i, '电话数量'] = y['资源来源'].count()
            df1.loc[i, '接通率'] = str(int((y[y['接通率'] == '接通']['接通率'].count() / y['接通率'].count()) * 100))+'%'
            df1.loc[i, '需求率'] = str(int((y[y['需求率'] == '需要']['需求率'].count() / y['需求率'].count()) * 100))+'%'
            i += 1

        df1 = df1.reset_index(drop=True)
        df1.loc[30, '资源名称'] = '电话总量'
        df1.loc[30, '电话数量'] = df1['电话数量'].sum()

        if no==0:
            df1.to_excel('C:\\Users\Administrator\Desktop\\每日资源数据统计.xlsx',index=False)
        elif no==1:
            df1.to_excel('C:\\Users\Administrator\Desktop\\每周资源数据统计.xlsx', index=False)