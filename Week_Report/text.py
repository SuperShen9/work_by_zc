# -*- coding: utf-8 -*-
# author：Super.Shen
import os
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1500)
from Week_Report.Func import yue

df_all = pd.read_excel('C:\\Users\Administrator\Desktop\\3.xlsx')

def run(df):
    df_run = pd.DataFrame()
    for x in range(0, df.shape[0]):
        df_run.loc[x, '电话量'] = df.loc[x, '电话量']
        df_run.loc[x, '昨日到期客户数'] = df.loc[x, '昨日到期客户数']
        df_run.loc[x, '昨日逾期客户数'] = df.loc[x, '昨日逾期客户数']
        df_run.loc[x, '续期客户量'] = df.loc[x, '续期客户量']
        df_run.loc[x, '持单总量'] = df.loc[x, '持单总量']

        df_run.loc[x, '自己电话+微信成功'] = df.loc[x, '电话+微信量（成功/总量）'].split('/')[0]
        df_run.loc[x, '自己电话+微信总量'] = df.loc[x, '电话+微信量（成功/总量）'].split('/')[1]

        df_run.loc[x, '电销+微信成功'] = df.loc[x, '电销+微信量（成功/总量）'].split('/')[0]
        df_run.loc[x, '电销+微信总量'] = df.loc[x, '电销+微信量（成功/总量）'].split('/')[1]

        df_run.loc[x, '不回'] = df.loc[x, '收单量（不回/不全/收全）'].split('/')[0]
        df_run.loc[x, '不全'] = df.loc[x, '收单量（不回/不全/收全）'].split('/')[1]
        df_run.loc[x, '收全'] = df.loc[x, '收单量（不回/不全/收全）'].split('/')[2]

        df_run.loc[x, '审核通过'] = df.loc[x, '审核通过/拒绝'].split('/')[0]
        df_run.loc[x, '审核拒绝'] = df.loc[x, '审核通过/拒绝'].split('/')[1]

        df_run.loc[x, '新单到期'] = df.loc[x, '每日新单到期还款情况'].split('/')[0]
        df_run.loc[x, '新单总量'] = df.loc[x, '每日新单到期还款情况'].split('/')[1]

        df_run.loc[x, '老单到期'] = df.loc[x, '每日老单到期还款情况'].split('/')[0]
        df_run.loc[x, '老单总量'] = df.loc[x, '每日老单到期还款情况'].split('/')[1]

        df_run.loc[x, '续借客户'] = df.loc[x, '续借率'].split('/')[0]
        df_run.loc[x, '续借总量'] = df.loc[x, '续借率'].split('/')[1]

    df_run[['电话量', '昨日到期客户数', '昨日逾期客户数', '续期客户量', '持单总量']] = df_run[
        ['电话量', '昨日到期客户数', '昨日逾期客户数', '续期客户量', '持单总量']].apply(pd.to_numeric)

    df_run[['自己电话+微信成功', '自己电话+微信总量', '电销+微信成功', '电销+微信总量', '不回', '不全', '收全', '审核通过', '审核拒绝', '新单到期', '新单总量', '老单到期',
            '老单总量', '续借客户', '续借总量']] = \
        df_run[
            ['自己电话+微信成功', '自己电话+微信总量', '电销+微信成功', '电销+微信总量', '不回', '不全', '收全', '审核通过', '审核拒绝', '新单到期', '新单总量', '老单到期',
             '老单总量', '续借客户', '续借总量']].apply(pd.to_numeric)

    # print(df_run['收全'] == df_run['审核通过'] + df_run['审核拒绝'])

    for col in df_run.columns:
        df_run.loc[20 + 1, col] = df_run[col].sum()

    df.loc[20, '电话+微信量（成功/总量）'] = str(int(df_run.loc[21]['自己电话+微信成功'])) + '/' + str(int(df_run.loc[21]['自己电话+微信总量']))
    # df.loc[21, '电话+微信量（成功/总量）'] = str(round((df_run.loc[21]['自己电话+微信成功'] / df_run.loc[21]['自己电话+微信总量']) * 100, 2)) + '%'

    df.loc[20, '电销+微信量（成功/总量）'] = str(int(df_run.loc[21]['电销+微信成功'])) + '/' + str(int(df_run.loc[21]['电销+微信总量']))
    # df.loc[21, '电销+微信量（成功/总量）'] = str(round((df_run.loc[21]['电销+微信成功'] / df_run.loc[21]['电销+微信总量']) * 100, 2)) + '%'

    df.loc[20, '收单量（不回/不全/收全）'] = str(int(df_run.loc[21]['不回'])) + '/' + str(int(df_run.loc[21]['不全'])) + '/' + str(
        int(df_run.loc[21]['收全']))
    # df.loc[21, '收单量（不回/不全/收全）'] = str(round(df_run.loc[21]['收全'] / (df_run.loc[21]['不回'] + df_run.loc[21]['不全'] + df_run.loc[21]['收全']) * 100,2)) + '%'

    df.loc[20, '审核通过/拒绝'] = str(int(df_run.loc[21]['审核通过'])) + '/' + str(int(df_run.loc[21]['审核拒绝']))
    # df.loc[21, '审核通过/拒绝'] = str(round(df_run.loc[21]['审核通过'] / (df_run.loc[21]['审核通过'] + df_run.loc[21]['审核拒绝']) * 100, 2)) + '%'

    df.loc[20, '每日新单到期还款情况'] = str(int(df_run.loc[21]['新单到期'])) + '/' + str(int(df_run.loc[21]['新单总量']))
    # df.loc[21, '每日新单到期还款情况'] = str(round((df_run.loc[21]['新单到期'] / df_run.loc[21]['新单总量']) * 100, 2)) + '%'

    df.loc[20, '每日老单到期还款情况'] = str(int(df_run.loc[21]['老单到期'])) + '/' + str(int(df_run.loc[21]['老单总量']))
    # df.loc[21, '每日老单到期还款情况'] = str(round((df_run.loc[21]['老单到期'] / df_run.loc[21]['老单总量']) * 100, 2)) + '%'

    df.loc[20, '续借率'] = str(int(df_run.loc[21]['续借客户'])) + '/' + str(int(df_run.loc[21]['续借总量']))
    # df.loc[21, '续借率'] = str(round((df_run.loc[21]['续借客户'] / df_run.loc[21]['续借总量']) * 100, 2)) + '%'

    df.loc[20, '电话量'] = df_run.loc[21]['电话量']
    df.loc[20, '昨日到期客户数'] = df_run.loc[21]['昨日到期客户数']
    df.loc[20, '昨日逾期客户数'] = df_run.loc[21]['昨日逾期客户数']
    df.loc[20, '续期客户量'] = df_run.loc[21]['续期客户量']
    df.loc[20, '持单总量'] = df_run.loc[21]['持单总量']

    df.loc[20, '审核员姓名'] = df.loc[0, '审核员姓名']
    df.loc[20, '日期'] = 'three'
    # df.loc[21, '审核员姓名'] = '成功比率'

    return df


df_all = df_all.groupby('审核员姓名')

df = pd.DataFrame()
for x, y in df_all:
    y = y.reset_index(drop=True)
    df = df.append(run(y), ignore_index=True)


# print(df[df['日期'] == 'three'])

df[df['日期'] == 'three'].to_excel('C:\\Users\Administrator\Desktop\\k.xlsx', index=False)