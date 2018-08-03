# -*- coding: utf-8 -*-
# author：Super.Shen

import os, openpyxl
import pandas as pd
from Daily.Func import yue,ri,ri_now
import datetime
hour = datetime.datetime.now().strftime('%H')

if len(yue) < 2:
    yue = '0' + yue
if len(ri_now) < 2:
    ri_now = '0' + ri_now
if len(ri) < 2:
    ri = '0' + ri


os.chdir('D:\Super\superflag')

wbf = openpyxl.load_workbook('数据合并.xlsx')

sheet = wbf['审核']

hang1 = sheet.max_row + 1

spam = {}
for row in range(2, hang1):
    flag = sheet['A' + str(row)].value.lower()
    number = sheet['B' + str(row)].value
    spam.setdefault(flag, number)

filepath = 'D:\Super\\每日报告合并'

os.chdir(filepath)
df = pd.DataFrame()

list1 = []
for x, y, excels in os.walk(filepath):
    len_fk = len(excels)
    for excel in excels:
        df1 = pd.read_excel(excel)
        df = df.append(df1)
        list1.append(excel.split('-')[1])

df = df.reset_index(drop=True)


# 筛选出不属于昨天的数据
df = df[df['审核员姓名'] != '张三']

if int(hour) > 11:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri_now))]
else:
    df = df[df['日期'] == pd.to_datetime('2018{}{}'.format(yue, ri))]

print('\n风控统计人数：{}\n'.format(len_fk))


if df.shape[0] != len_fk:
    error = [l for l in list1 if l not in list(df['审核员姓名'])]
    print('\n{} 的日期有问题，请核对!'.format(error))

else:

    df.to_excel('C:\\Users\Administrator\Desktop\k.xlsx'.format(yue, ri_now), index=False)

    excel = 'C:\\Users\Administrator\Desktop\k.xlsx'

    df = pd.read_excel(excel)

    df_check = pd.DataFrame()

    df_run = pd.DataFrame()

    exit_count=0
    for x in range(0, df.shape[0]):
        try:
            df_check.loc[x, '审核员姓名'] = df.loc[x, '审核员姓名']

            df_run.loc[x, '日期'] = df.loc[x, '日期']
            df_run.loc[x, '审核员姓名'] = df.loc[x, '审核员姓名']

            df_run.loc[x, '电话量'] = df.loc[x, '电话量']

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

            df_run.loc[x, '昨日到期客户数'] = df.loc[x, '昨日到期客户数']
            df_run.loc[x, '昨日逾期客户数'] = df.loc[x, '昨日逾期客户数']
            df_run.loc[x, '续期客户量'] = df.loc[x, '续期客户量']

            df_run.loc[x, '续借客户'] = df.loc[x, '续借率'].split('/')[0]
            df_run.loc[x, '续借总量'] = df.loc[x, '续借率'].split('/')[1]

            df_run.loc[x, '持单总量'] = df.loc[x, '持单总量']

        except IndexError:
            exit_count += 1
            print('{} 数据填写错误\n'.format(df_check.loc[x, '审核员姓名']))
            continue

    if exit_count >= 1:
        exit()

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

    df_check['电话量乱填'] = (df_run['自己电话+微信总量'] <= 60).apply(lambda x: pan(x))
    df_check['电话+微信检测'] = (df_run['自己电话+微信成功'] <= df_run['自己电话+微信总量']).apply(lambda x: pan(x))
    df_check['电销+微信检测'] = (df_run['电销+微信成功'] <= df_run['电销+微信总量']).apply(lambda x: pan(x))
    df_check['收全检测'] = (df_run['收全'] == df_run['审核通过'] + df_run['审核拒绝']).apply(lambda x: pan(x))
    df_check['新单到期检测'] = (df_run['新单到期'] <= df_run['新单总量']).apply(lambda x: pan(x))
    df_check['老单到期检测'] = (df_run['老单到期'] <= df_run['老单总量']).apply(lambda x: pan(x))
    df_check['续借检测'] = (df_run['续借客户'] <= df_run['续借总量']).apply(lambda x: pan(x))
    # df_check['续借检测2'] = (df_run['新单到期']+df_run['老单到期'] ==df_run['续借总量']).apply(lambda x: pan(x))


    df_upload=df_run.copy()
    df_upload.columns=['日期','审核员姓名','电话量','电话+微信量（成功）','电话+微信量(总量)','电销+微信量（成功）',
                       '电销+微信量(总量)','收单量（不回）','收单量(不全)','收单量(收全)','审核通过','审核拒绝',
                       '每日新单到期还款','每日新单到期待还款总量','每日老单到期还款','每日老单到期待还款总量',
                       '昨日到期客户数','昨日逾期客户数','续期客户量','续借客户量','到期还款客户数量','持单总量']
    # 风控检测结果
    df_check.to_excel('C:\\Users\Administrator\Desktop\风控部门错误标记.xlsx')
    # df_upload.to_excel('C:\\Users\Administrator\Desktop\风控-{}{}-上传.xlsx'.format(yue, ri_now),index=False)
    # print(df_check.shape[0], df_check.shape[1])

    error_count = 0
    for x in range(df_check.shape[0]):
       for y in range(df_check.shape[1]):
           if df_check.iat[x, y] != '':
               error_count += 1

    if error_count == df_check.shape[0]:
        pass
    else:
        print(df_check)
        exit()

    # 每一个分裂进行计算
    for col in df_run.columns[2:]:
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

    df_new = df[['日期', '审核员姓名', '每日新单到期还款情况', '每日老单到期还款情况']]

    df = df.reset_index(drop=True)
    len_dx = df.shape[0]
    len_new = df.shape[0] - 1
    i = 20
    df.loc[len_dx + i + 1, '日期'] = ''
    df.loc[len_dx + i + 2, '日期'] = ''
    df.loc[len_dx + i + 3, '日期'] = 'Flag'
    df.loc[len_dx + i + 3, '审核员姓名'] = '审核汇总'
    df.loc[len_dx + i + 3, '电话量'] = '成功比率'

    k = 4
    for col in df.columns[2:]:
        df.loc[len_dx + i + k, '日期'] = col
        df.loc[len_dx + i + k, '审核员姓名'] = df.loc[len_new-1, col]
        df.loc[len_dx + i + k, '电话量'] = df.loc[len_new, col]
        k += 1



    if int(hour) > 10:
        df.to_excel('C:\\Users\Administrator\Desktop\风控部门{}月{}日报告.xlsx'.format(yue, ri_now), index=False)
    else:
        df_new.to_excel('C:\\Users\Administrator\Desktop\风控{}月{}日新老单跟新.xlsx'.format(yue, ri), index=False)
        os.mkdir('昨日新老单')

    print('\n没有问题，统计已存放桌面！')