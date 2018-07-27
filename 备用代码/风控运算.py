# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1500)

from Daily.Func import yue,ri_now

excel = 'C:\\Users\Administrator\Desktop\k.xlsx'

df = pd.read_excel(excel)

# exit()
df_check = pd.DataFrame()

df_run = pd.DataFrame()
for x in range(0, df.shape[0]):
    df_check.loc[x, '审核员姓名'] = df.loc[x, '审核员姓名']
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



df_run[['电话量','昨日到期客户数','昨日逾期客户数','续期客户量','持单总量']] = df_run[['电话量','昨日到期客户数','昨日逾期客户数','续期客户量','持单总量']].apply(pd.to_numeric)

df_run[['自己电话+微信成功','自己电话+微信总量', '电销+微信成功','电销+微信总量', '不回', '不全', '收全','审核通过','审核拒绝','新单到期','新单总量','老单到期','老单总量','续借客户','续借总量']] =\
    df_run[['自己电话+微信成功','自己电话+微信总量', '电销+微信成功','电销+微信总量', '不回', '不全', '收全','审核通过','审核拒绝','新单到期','新单总量','老单到期','老单总量','续借客户','续借总量']].apply(pd.to_numeric)


def pan(x):
    if x==True:
        x=''
    return x

df_check['电话量乱填'] = (df_run['自己电话+微信总量'] <= 60).apply(lambda x:pan(x))
df_check['电话+微信检测'] = (df_run['自己电话+微信成功'] <= df_run['自己电话+微信总量']).apply(lambda x:pan(x))
df_check['电销+微信检测'] = (df_run['电销+微信成功'] <= df_run['电销+微信总量']).apply(lambda x:pan(x))
df_check['收全检测'] = (df_run['收全'] == df_run['审核通过']+df_run['审核拒绝']).apply(lambda x:pan(x))
df_check['新单到期检测'] = (df_run['新单到期'] <= df_run['新单总量']).apply(lambda x:pan(x))
df_check['老单到期检测'] = (df_run['老单到期'] <= df_run['老单总量']).apply(lambda x:pan(x))
df_check['续借检测'] = (df_run['续借客户'] <= df_run['续借总量']).apply(lambda x:pan(x))


# 风控检测结果
df_check.to_excel('C:\\Users\Administrator\Desktop\风控部门错误标记.xlsx')

for col in df_run.columns:
    df_run.loc[20 + 1, col] = df_run[col].sum()

df.loc[20, '电话+微信量（成功/总量）'] = str(int(df_run.loc[21]['自己电话+微信成功']))+'/'+str(int(df_run.loc[21]['自己电话+微信总量']))
df.loc[21, '电话+微信量（成功/总量）'] = str(round((df_run.loc[21]['自己电话+微信成功']/df_run.loc[21]['自己电话+微信总量'])*100, 2))+'%'

df.loc[20, '电销+微信量（成功/总量）'] = str(int(df_run.loc[21]['电销+微信成功']))+'/'+str(int(df_run.loc[21]['电销+微信总量']))
df.loc[21, '电销+微信量（成功/总量）'] = str(round((df_run.loc[21]['电销+微信成功']/df_run.loc[21]['电销+微信总量'])*100, 2))+'%'

df.loc[20, '收单量（不回/不全/收全）'] = str(int(df_run.loc[21]['不回']))+'/'+str(int(df_run.loc[21]['不全']))+'/'+str(int(df_run.loc[21]['收全']))
df.loc[21, '收单量（不回/不全/收全）'] = str(round(df_run.loc[21]['收全']/(df_run.loc[21]['不回']+df_run.loc[21]['不全']+df_run.loc[21]['收全'])*100, 2))+'%'

df.loc[20, '审核通过/拒绝'] = str(int(df_run.loc[21]['审核通过']))+'/'+str(int(df_run.loc[21]['审核拒绝']))
df.loc[21, '审核通过/拒绝'] = str(round(df_run.loc[21]['审核通过']/(df_run.loc[21]['审核通过']+df_run.loc[21]['审核拒绝'])*100, 2))+'%'

df.loc[20, '每日新单到期还款情况'] = str(int(df_run.loc[21]['新单到期']))+'/'+str(int(df_run.loc[21]['新单总量']))
df.loc[21, '每日新单到期还款情况'] = str(round((df_run.loc[21]['新单到期']/df_run.loc[21]['新单总量'])*100, 2))+'%'

df.loc[20, '每日老单到期还款情况'] = str(int(df_run.loc[21]['老单到期']))+'/'+str(int(df_run.loc[21]['老单总量']))
df.loc[21, '每日老单到期还款情况'] = str(round((df_run.loc[21]['老单到期']/df_run.loc[21]['老单总量'])*100, 2))+'%'

df.loc[20, '续借率'] = str(int(df_run.loc[21]['续借客户']))+'/'+str(int(df_run.loc[21]['续借总量']))
df.loc[21, '续借率'] = str(round((df_run.loc[21]['续借客户']/df_run.loc[21]['续借总量'])*100, 2))+'%'

df.loc[20, '电话量'] = df_run.loc[21]['电话量']
df.loc[20, '昨日到期客户数'] = df_run.loc[21]['昨日到期客户数']
df.loc[20, '昨日逾期客户数'] = df_run.loc[21]['昨日逾期客户数']
df.loc[20, '续期客户量'] = df_run.loc[21]['续期客户量']
df.loc[20, '持单总量'] = df_run.loc[21]['持单总量']

df.loc[20, '审核员姓名'] = '数据汇总'
df.loc[21, '审核员姓名'] = '成功比率'

df.to_excel('C:\\Users\Administrator\Desktop\风控部门{}月{}日报告.xlsx'.format(yue, ri_now), index=False)
