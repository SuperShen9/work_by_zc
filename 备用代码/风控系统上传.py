# -*- coding: utf-8 -*-
# author：Super.Shen

import os
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1500)
path = 'C:\\Users\Administrator\Desktop\风控部门07月09日报告.xlsx'
df =pd.read_excel(path)
df.dropna(how='any', inplace=True)

df_run = pd.DataFrame()
for x in range(0, df.shape[0]):
    df_run.loc[x, '日期'] = df.loc[x, '日期']
    df_run.loc[x, '审核员姓名'] = df.loc[x, '审核员姓名']
    df_run.loc[x, '电话量'] = df.loc[x, '电话量']

    df_run.loc[x, '自己电话+微信成功'] = df.loc[x, '电话+微信量（成功/总量）'].split('/')[0]
    df_run.loc[x, '自己电话+微信总量'] = df.loc[x, '电话+微信量（成功/总量）'].split('/')[1]

    df_run.loc[x, '电销+微信成功'] = df.loc[x, '电销+微信量（成功/总量）'].split('/')[0]
    df_run.loc[x, '电销+微信总量'] = df.loc[x, '电销+微信量（成功/总量）'].split('/')[1]

    df_run.loc[x, '收单量不回'] = df.loc[x, '收单量（不回/不全/收全）'].split('/')[0]
    df_run.loc[x, '收单量不全'] = df.loc[x, '收单量（不回/不全/收全）'].split('/')[1]
    df_run.loc[x, '收单量收全'] = df.loc[x, '收单量（不回/不全/收全）'].split('/')[2]

    df_run.loc[x, '审核通过'] = df.loc[x, '审核通过/拒绝'].split('/')[0]
    df_run.loc[x, '审核拒绝'] = df.loc[x, '审核通过/拒绝'].split('/')[1]

    df_run.loc[x, '新单到期'] = df.loc[x, '每日新单到期还款情况'].split('/')[0]
    df_run.loc[x, '新单总量'] = df.loc[x, '每日新单到期还款情况'].split('/')[1]

    df_run.loc[x, '老单到期'] = df.loc[x, '每日老单到期还款情况'].split('/')[0]
    df_run.loc[x, '老单总量'] = df.loc[x, '每日老单到期还款情况'].split('/')[1]

    df_run.loc[x, '昨日到期客户数'] = df.loc[x, '昨日到期客户数']
    df_run.loc[x, '昨日逾期客户数'] = df.loc[x, '昨日逾期客户数']
    df_run.loc[x, '续期客户量'] = df.loc[x, '续期客户量']

    df_run.loc[x, '续借客户'] = df.loc[x, '续借率'].split('/')[0]
    df_run.loc[x, '续借总量'] = df.loc[x, '续借率'].split('/')[1]


    df_run.loc[x, '持单总量'] = df.loc[x, '持单总量']


df_run.to_excel('C:\\Users\Administrator\Desktop\风控部门系统上传.xlsx', index=False)