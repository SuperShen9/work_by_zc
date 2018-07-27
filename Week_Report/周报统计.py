# -*- coding: utf-8 -*-
# author：Super.Shen
import os
import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1500)
from Week_Report.Func import yue

week = input('\n{}月第几周？\n'.format(yue))


# 文件路径
file_path ='D:\Super\week_hebing'
# 切换路径
os.chdir(file_path)
# 取出文件列表
file_list = os.listdir(file_path)
# 监测文件是否为同一部门
list1 = []
for i in file_list:
    list1.append(i[:2])
bm = list1[0]
df1 = pd.DataFrame({'xxx': list1})

def dianxiao_week():
    # i作为增量用于df的最后一行
    i = 20
    # 读取数据
    df_all = pd.DataFrame()
    for file in file_list:
        df = pd.read_excel(file_path + '\\' + file)
        df_all = df_all.append(df, ignore_index=True)

    df_all.dropna(how='any', inplace=True)

    # # 新系统-统计
    # df_all.to_excel('C:\\Users\Administrator\Desktop\dianxiao_Data.xlsx',index=False)
    # exit()

    df_all = df_all.groupby('电销姓名').sum()

    df_all = df_all[df_all.columns[:-2]]

    df_all.reset_index(inplace=True)

    len_dx = df_all.shape[0]

    df_all = df_all.reset_index(drop=True)

    df_all.loc[len_dx + i, '电销姓名'] = '电销汇总'

    for col in df_all.columns[1:]:
        df_all.loc[len_dx + i, col] = df_all[col].sum()

    df_all['提交率'] = df_all['提交客户'] / df_all['已打资源']
    df_all['成交率'] = df_all['成交客户'] / df_all['已打资源']

    df_all = df_all.reset_index(drop=True)

    len_new =df_all.shape[0]-1

    df_all.loc[len_dx + i + 1, '电销姓名'] = ''
    df_all.loc[len_dx + i + 2, '电销姓名'] = ''
    df_all.loc[len_dx + i + 3, '电销姓名'] = 'Flag'
    df_all.loc[len_dx + i + 3, '收到资源'] = '电销汇总'
    # print(df_all)
    # exit()

    k = 4
    for col in df_all.columns[1:]:
        df_all.loc[len_dx + i + k, '电销姓名'] = col
        df_all.loc[len_dx + i + k, '收到资源'] = df_all.loc[len_new, col]
        k += 1

    if week == str(5):
        df_all.to_excel('C:\\Users\Administrator\Desktop\{}部门{}月 - 月报.xlsx'.format(bm, yue), index=False)
    else:
        df_all.to_excel('C:\\Users\Administrator\Desktop\{}部门{}月第{}周-周报.xlsx'.format(bm, yue, week), index=False)

def cuishou_week():
    # i作为增量用于df的最后一行
    i = 20
    # 读取数据
    df_all = pd.DataFrame()
    for file in file_list:
        df = pd.read_excel(file_path + '\\' + file)
        df_all = df_all.append(df, ignore_index=True)

    df_all.dropna(how='any', inplace=True)

    # #新系统数据统计
    # df_all.to_excel('C:\\Users\Administrator\Desktop\cuishou_Data.xlsx',index=False)
    # exit()

    df_all = df_all.groupby('催收员姓名').sum()

    df_all.reset_index(inplace=True)

    len_dx = df_all.shape[0]

    df_all.loc[len_dx + i, '催收员姓名'] = '催收汇总'

    for col in df_all.columns[1:]:
        df_all.loc[len_dx + i, col] = df_all[col].sum()

    # 汇总新增字段
    df_all = df_all.reset_index(drop=True)

    len_new = df_all.shape[0] - 1

    df_all.loc[len_dx + i + 1, '催收员姓名'] = ''
    df_all.loc[len_dx + i + 2, '催收员姓名'] = ''
    df_all.loc[len_dx + i + 3, '催收员姓名'] = 'Flag'
    df_all.loc[len_dx + i + 3, '逾期总量'] = '催收汇总'
    # print(df_all)
    # exit()

    k = 4
    for col in df_all.columns[1:]:
        df_all.loc[len_dx + i + k, '催收员姓名'] = col
        df_all.loc[len_dx + i + k, '逾期总量'] = df_all.loc[len_new, col]
        k += 1
    if week == str(5):
        df_all.to_excel('C:\\Users\Administrator\Desktop\{}部门{}月-月报.xlsx'.format(bm, yue), index=False)
    else:
        df_all.to_excel('C:\\Users\Administrator\Desktop\{}部门{}月第{}周-周报.xlsx'.format(bm, yue, week), index=False)

from Func import fengkong_run,zong_run
def fengkong_week():
    # i作为增量用于df的最后一行
    i = 20
    # 读取数据
    df_all = pd.DataFrame()
    for file in file_list:
        df = pd.read_excel(file_path + '\\' + file)
        df_all = df_all.append(df, ignore_index=True)

    df_all.dropna(how='any', inplace=True)

    # # 新系统数据统计
    # df_all.to_excel('C:\\Users\Administrator\Desktop\\fengkong_Data.xlsx', index=False)
    # exit()

    df_all = df_all.groupby('审核员姓名')

    df_hz = pd.DataFrame()

    for x, y in df_all:
        y.reset_index(inplace=True)
        # print(y)
        # print(fengkong_run(y))
        # y.to_excel('C:\\Users\Administrator\Desktop\k.xlsx',index=False)
        # print(fengkong_run(y).tail(1))
        df_hz = df_hz.append(fengkong_run(y).tail(1), ignore_index=True)

    df_hz = df_hz[df.columns[1:]]

    df = zong_run(df_hz)
    if week == str(5):
        df.to_excel('C:\\Users\Administrator\Desktop\风控部门{}月-月报.xlsx'.format(yue), index=False)
    else:
        df.to_excel('C:\\Users\Administrator\Desktop\风控部门{}月第{}周-周报.xlsx'.format(yue, week), index=False)


if df1.drop_duplicates().shape[0] == 1:
    if bm == '电销':
        dianxiao_week()
    elif bm == '催收':
        cuishou_week()
    elif bm == '风控':
        fengkong_week()
else:
    print('存在不同部门，请检查文件！')


