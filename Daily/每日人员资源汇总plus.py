# -*- coding: utf-8 -*-
# author：Super.Shen
import pandas as pd
import os
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

file1 = 'C:\\Users\Administrator\Desktop\Feedback_Data.xlsx'
file2 = 'C:\\Users\Administrator\Desktop\Week_Data.xlsx'

list1 = [file1, file2]


def run(no, x, y):
    y = y.reset_index(drop=True)
    df1.loc[no, '部门'] = y.loc[0, '部门']
    df1.loc[no, '姓名'] = x
    df1.loc[no, '电话数量'] = y['姓名'].count()
    df1.loc[no, '接通量'] = y[y['接通率'] == '接通']['姓名'].count()
    df1.loc[no, '接通率'] = str(int((y[y['接通率'] == '接通']['接通率'].count() / y['接通率'].count()) * 100)) + '%'

    df1.loc[no, '需求量'] = y[y['需求率'] == '需要']['姓名'].count()
    df1.loc[no, '需求率'] = str(int((y[y['需求率'] == '需要']['需求率'].count() / y['需求率'].count()) * 100)) + '%'

    df1.loc[no, '下单量'] = y[y['下单率'] == '下单']['姓名'].count()
    df1.loc[no, '下单率'] = str(int((y[y['下单率'] == '下单']['下单率'].count() / y['下单率'].count()) * 100)) + '%'
    no += 1

# 统计每个业务员的数据
for no, i in enumerate(list1):
    if os.path.exists(i):
        df = pd.read_excel(i)

        # 统计接通率/需求率
        i = 0
        df1 = pd.DataFrame()
        for x, y in df.groupby(['姓名']):
            run(i, x, y)
            i += 1

        df1.sort_values(by='部门',  inplace=True)

        # 两个部门单独统计
        ii = df1.shape[0]+1
        for x, y in df.groupby(['部门']):
            run(ii, x, y)
            ii += 1

        # 资源单独统计
        iii = df1.shape[0] + 1
        for x, y in df.groupby(['资源来源']):
            run(iii, x, y)
            iii += 1

        df1 = df1.reset_index(drop=True)
        # print(df1)
        # exit()

        if no==0:
            df1.to_excel('C:\\Users\Administrator\Desktop\\每日电话拨打统计.xlsx',index=False)
        elif no==1:
            df1.to_excel('C:\\Users\Administrator\Desktop\\每周电话数据统计.xlsx', index=False)