# -*- coding: utf-8 -*-
# author：Super.Shen
from datetime import *
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1500)

time1 = datetime.today()
nian = str(time1.year)
yue = str(time1.month)
ri = str(time1.day-1)
ri_zhou = str(time1.day-5)
ri_now = str(time1.day)

if len(yue) < 2:
    yue = '0' + yue
if len(ri_now) < 2:
    ri_now = '0' + ri_now
if len(ri) < 2:
    ri = '0' + ri
if len(ri_zhou) < 2:
    ri_zhou = '0' + ri_zhou


ri_now = str(time1.day)
def fengkong_run(df):
    df_check = pd.DataFrame()

    df_run = pd.DataFrame()
    for x in range(0, df.shape[0]):
        # print(df.shape[0])
        # exit()
        df_run.loc[x, '审核员姓名'] = df.loc[x, '审核员姓名']
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

    i=40
    for col in df_run.columns:
        df_run.loc[i + 1, col] = df_run[col].sum()

    df.loc[i, '电话+微信量（成功/总量）'] = str(int(df_run.loc[i+1]['自己电话+微信成功'])) + '/' + str(int(df_run.loc[i+1]['自己电话+微信总量']))
    # df.loc[i+1, '电话+微信量（成功/总量）'] = str(round((df_run.loc[i+1]['自己电话+微信成功'] / df_run.loc[i+1]['自己电话+微信总量']) * 100, 2)) + '%'

    df.loc[i, '电销+微信量（成功/总量）'] = str(int(df_run.loc[i+1]['电销+微信成功'])) + '/' + str(int(df_run.loc[i+1]['电销+微信总量']))
    # df.loc[i+1, '电销+微信量（成功/总量）'] = str(round((df_run.loc[i+1]['电销+微信成功'] / df_run.loc[i+1]['电销+微信总量']) * 100, 2)) + '%'

    df.loc[i, '收单量（不回/不全/收全）'] = str(int(df_run.loc[i+1]['不回'])) + '/' + str(int(df_run.loc[i+1]['不全'])) + '/' + str(
        int(df_run.loc[i+1]['收全']))
    # df.loc[i+1, '收单量（不回/不全/收全）'] = str(
    #     round(df_run.loc[i+1]['收全'] / (df_run.loc[i+1]['不回'] + df_run.loc[i+1]['不全'] + df_run.loc[i+1]['收全']) * 100,
    #           2)) + '%'

    df.loc[i, '审核通过/拒绝'] = str(int(df_run.loc[i+1]['审核通过'])) + '/' + str(int(df_run.loc[i+1]['审核拒绝']))
    # df.loc[i+1, '审核通过/拒绝'] = str(
    #     round(df_run.loc[i+1]['审核通过'] / (df_run.loc[i+1]['审核通过'] + df_run.loc[i+1]['审核拒绝']) * 100, 2)) + '%'

    df.loc[i, '每日新单到期还款情况'] = str(int(df_run.loc[i+1]['新单到期'])) + '/' + str(int(df_run.loc[i+1]['新单总量']))
    # df.loc[i+1, '每日新单到期还款情况'] = str(round((df_run.loc[i+1]['新单到期'] / df_run.loc[i+1]['新单总量']) * 100, 2)) + '%'

    df.loc[i, '每日老单到期还款情况'] = str(int(df_run.loc[i+1]['老单到期'])) + '/' + str(int(df_run.loc[i+1]['老单总量']))
    # df.loc[i+1, '每日老单到期还款情况'] = str(round((df_run.loc[i+1]['老单到期'] / df_run.loc[i+1]['老单总量']) * 100, 2)) + '%'

    df.loc[i, '续借率'] = str(int(df_run.loc[i+1]['续借客户'])) + '/' + str(int(df_run.loc[i+1]['续借总量']))
    # df.loc[i+1, '续借率'] = str(round((df_run.loc[i+1]['续借客户'] / df_run.loc[i+1]['续借总量']) * 100, 2)) + '%'

    df.loc[i, '电话量'] = df_run.loc[i+1]['电话量']
    df.loc[i, '昨日到期客户数'] = df_run.loc[i+1]['昨日到期客户数']
    df.loc[i, '昨日逾期客户数'] = df_run.loc[i+1]['昨日逾期客户数']
    df.loc[i, '续期客户量'] = df_run.loc[i+1]['续期客户量']
    df.loc[i, '持单总量'] = df_run.loc[i+1]['持单总量']

    df.loc[i, '审核员姓名'] = df.loc[0, '审核员姓名']

    df = df.reset_index(drop=True)
    # print(df)
    # exit()

    return df


def zong_run(df):

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

    df_run[['电话量', '昨日到期客户数', '昨日逾期客户数', '续期客户量', '持单总量']] = df_run[
        ['电话量', '昨日到期客户数', '昨日逾期客户数', '续期客户量', '持单总量']].apply(pd.to_numeric)

    df_run[['自己电话+微信成功', '自己电话+微信总量', '电销+微信成功', '电销+微信总量', '不回', '不全', '收全', '审核通过', '审核拒绝', '新单到期', '新单总量', '老单到期',
            '老单总量', '续借客户', '续借总量']] = \
        df_run[
            ['自己电话+微信成功', '自己电话+微信总量', '电销+微信成功', '电销+微信总量', '不回', '不全', '收全', '审核通过', '审核拒绝', '新单到期', '新单总量', '老单到期',
             '老单总量', '续借客户', '续借总量']].apply(pd.to_numeric)

    def pan(x):
        if x == True:
            x = ''
        return x

    df_check['电话量填在微信'] = (df_run['自己电话+微信总量'] <= 400).apply(lambda x: pan(x))
    df_check['电话+微信检测'] = (df_run['自己电话+微信成功'] <= df_run['自己电话+微信总量']).apply(lambda x: pan(x))
    df_check['电销+微信检测'] = (df_run['电销+微信成功'] <= df_run['电销+微信总量']).apply(lambda x: pan(x))
    df_check['收全检测'] = (df_run['收全'] == df_run['审核通过'] + df_run['审核拒绝']).apply(lambda x: pan(x))
    df_check['新单到期检测'] = (df_run['新单到期'] <= df_run['新单总量']).apply(lambda x: pan(x))
    df_check['老单到期检测'] = (df_run['老单到期'] <= df_run['老单总量']).apply(lambda x: pan(x))
    df_check['续借检测'] = (df_run['续借客户'] <= df_run['续借总量']).apply(lambda x: pan(x))

    # 风控检测结果
    # print(df_check)
    # df_check.to_excel('C:\\Users\Administrator\Desktop\风控部门错误标记-周.xlsx')

    for col in df_run.columns:
        df_run.loc[20 + 1, col] = df_run[col].sum()

    df.loc[20, '电话+微信量（成功/总量）'] = str(int(df_run.loc[21]['自己电话+微信成功'])) + '/' + str(int(df_run.loc[21]['自己电话+微信总量']))
    df.loc[21, '电话+微信量（成功/总量）'] = str(round((df_run.loc[21]['自己电话+微信成功'] / df_run.loc[21]['自己电话+微信总量']) * 100, 2)) + '%'

    df.loc[20, '电销+微信量（成功/总量）'] = str(int(df_run.loc[21]['电销+微信成功'])) + '/' + str(int(df_run.loc[21]['电销+微信总量']))
    df.loc[21, '电销+微信量（成功/总量）'] = str(round((df_run.loc[21]['电销+微信成功'] / df_run.loc[21]['电销+微信总量']) * 100, 2)) + '%'

    df.loc[20, '收单量（不回/不全/收全）'] = str(int(df_run.loc[21]['不回'])) + '/' + str(int(df_run.loc[21]['不全'])) + '/' + str(
        int(df_run.loc[21]['收全']))
    df.loc[21, '收单量（不回/不全/收全）'] = str(
        round(df_run.loc[21]['收全'] / (df_run.loc[21]['不回'] + df_run.loc[21]['不全'] + df_run.loc[21]['收全']) * 100,
              2)) + '%'

    df.loc[20, '审核通过/拒绝'] = str(int(df_run.loc[21]['审核通过'])) + '/' + str(int(df_run.loc[21]['审核拒绝']))
    df.loc[21, '审核通过/拒绝'] = str(
        round(df_run.loc[21]['审核通过'] / (df_run.loc[21]['审核通过'] + df_run.loc[21]['审核拒绝']) * 100, 2)) + '%'

    df.loc[20, '每日新单到期还款情况'] = str(int(df_run.loc[21]['新单到期'])) + '/' + str(int(df_run.loc[21]['新单总量']))
    df.loc[21, '每日新单到期还款情况'] = str(round((df_run.loc[21]['新单到期'] / df_run.loc[21]['新单总量']) * 100, 2)) + '%'

    df.loc[20, '每日老单到期还款情况'] = str(int(df_run.loc[21]['老单到期'])) + '/' + str(int(df_run.loc[21]['老单总量']))
    df.loc[21, '每日老单到期还款情况'] = str(round((df_run.loc[21]['老单到期'] / df_run.loc[21]['老单总量']) * 100, 2)) + '%'

    df.loc[20, '续借率'] = str(int(df_run.loc[21]['续借客户'])) + '/' + str(int(df_run.loc[21]['续借总量']))
    df.loc[21, '续借率'] = str(round((df_run.loc[21]['续借客户'] / df_run.loc[21]['续借总量']) * 100, 2)) + '%'

    df.loc[20, '电话量'] = df_run.loc[21]['电话量']
    df.loc[20, '昨日到期客户数'] = df_run.loc[21]['昨日到期客户数']
    df.loc[20, '昨日逾期客户数'] = df_run.loc[21]['昨日逾期客户数']
    df.loc[20, '续期客户量'] = df_run.loc[21]['续期客户量']
    df.loc[20, '持单总量'] = df_run.loc[21]['持单总量']

    df.loc[20, '审核员姓名'] = '数据汇总'
    df.loc[21, '审核员姓名'] = '成功比率'

    # 汇总新增字段
    i = 20
    df_all = df.reset_index(drop=True)

    len_new = df_all.shape[0] - 1
    len_dx = df_all.shape[0]

    df_all.loc[len_dx + i + 1, '审核员姓名'] = ''
    df_all.loc[len_dx + i + 2, '审核员姓名'] = ''
    df_all.loc[len_dx + i + 3, '审核员姓名'] = 'Flag'
    df_all.loc[len_dx + i + 3, '电话量'] = '风控汇总'
    df_all.loc[len_dx + i + 3, '电话+微信量（成功/总量）'] = '成功比例'
    # print(df_all)
    # exit()

    k = 4
    for col in df_all.columns[1:]:
        df_all.loc[len_dx + i + k, '审核员姓名'] = col
        df_all.loc[len_dx + i + k, '电话量'] = df_all.loc[len_new-1, col]
        df_all.loc[len_dx + i + k, '电话+微信量（成功/总量）'] = df_all.loc[len_new, col]
        k += 1

    return df_all



import pandas as pd
import os
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

def Statistic():

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