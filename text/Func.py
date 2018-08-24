# -*- coding: utf-8 -*-
# author：Super.Shen
import pandas as pd
import numpy as np
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000) #显示1000行


def read_data():
    df = pd.read_excel('C:\\Users\Administrator\Desktop\pandas.xlsx')
    count = 0
    df_all = pd.DataFrame()
    for i in range(df.shape[0]):
        try:
            content = df.loc[i, 'content']
            content = content[content.find('[{"approv'):content.find('}],"querySt')+2]
            df1 = pd.read_json(content)
            df1['tel'] = df.loc[i, 'mobile']
            df1['Flag'] = df.loc[i,  'Flag']
            df_all = df_all.append(df1, ignore_index=True, sort=True)
        except ValueError:
            count += 1

    print('error hang:{}'.format(count))
    print('data count：{}'.format(df_all.shape[0]))
    df_all.to_hdf('C:\\Users\Administrator\Desktop\pandas.h5', key='data')

def return_data():
    # df = pd.read_hdf('C:\\Users\Administrator\Desktop\pandas.h5')
    # df.to_excel('C:\\Users\Administrator\Desktop\\file.xlsx')
    # exit()
    df = pd.read_excel('C:\\Users\Administrator\Desktop\\file.xlsx')

    # # 求出每个人每次申请金额的平均值
    df['min'] = df['loanAmount'].apply(lambda x: x[1: -1].split(',')[0])
    df['max'] = df['loanAmount'].apply(lambda x: x[1: -1].split(',')[1].replace('+', '0'))
    df['ave'] = (df['min'].apply(lambda x: int(x)) + df['max'].apply(lambda x: int(x))) / 2

    # # 每个电话的总申请量
    series1 = df.groupby('tel').size()
    series2 = df.groupby('tel')['periods'].mean()
    series3 = df.groupby('tel')['ave'].mean()

    series4 = df[df['shenpi'] == 1].groupby('tel')['shenpi'].size()
    series5 = df[df['shenpi'] == 0].groupby('tel')['shenpi'].size()

    df1 = pd.DataFrame([series1, series2, series3, series4, series5]).T
    df1.reset_index(inplace=True)
    df1.columns = ['Tel', 'size', 'periods', 'ave_cash', 'shenpi_1', 'shenpi_0']
    df1.fillna(value=0, inplace=True)

    df1.to_hdf('C:\\Users\Administrator\Desktop\\file.h5', key='data')

# read_data()
return_data()