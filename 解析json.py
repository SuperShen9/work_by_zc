# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

df = pd.read_excel('C:\\Users\Administrator\Desktop\李永杰\\beike.xlsx')


for i in range(df.shape[0]):
    content = df.loc[i,'data']
    content = pd.read_json(content)
    # print(i,content.loc['borrow_detail', 'JIE_DAI_BAO_LOAN'])
    df.loc[i, '借贷宝'] = content.loc['borrow_detail', 'JIE_DAI_BAO_LOAN']
    df.loc[i, '展期'] = content.loc['allroll_tip', 'JIE_DAI_BAO_LOAN']

    df.loc[i, '无忧'] = content.loc['note', 'WU_YOU_LOAN']

    df.loc[i, '今借到备注'] = content.loc['note', 'JIN_JIE_DAO_LOAN']
    df.loc[i, '当前逾期'] = content.loc['n_current_overdue_amt', 'JIN_JIE_DAO_LOAN']
    df.loc[i, '历史逾期金额'] = content.loc['n_overdue_amt', 'JIN_JIE_DAO_LOAN']
    df.loc[i, '7天逾期金额'] = content.loc['n_overdue_7days_amt', 'JIN_JIE_DAO_LOAN']
    df.loc[i, '借入笔数'] = content.loc['n_borrow_cnt', 'JIN_JIE_DAO_LOAN']
    df.loc[i, '借入人数'] = content.loc['n_borrow_people_num', 'JIN_JIE_DAO_LOAN']

df.to_excel('C:\\Users\Administrator\Desktop\\text1.xlsx')
exit()

# content = df.loc[0,'data']
# content = pd.read_json(content)
# content.to_excel('C:\\Users\Administrator\Desktop\\text1.xlsx')
# exit()

# 借贷宝
print(content.loc['borrow_detail', 'JIE_DAI_BAO_LOAN'])
# 展期
print(content.loc['allroll_tip', 'JIE_DAI_BAO_LOAN'])

# 无忧逾期
print(content.loc['note', 'WU_YOU_LOAN'])

# 今借到备注
print(content.loc['note', 'JIN_JIE_DAO_LOAN'])
# 今借到当前逾期
print(content.loc['n_current_overdue_amt', 'JIN_JIE_DAO_LOAN'])
# 历史逾期金额
print(content.loc['n_overdue_amt', 'JIN_JIE_DAO_LOAN'])
# 7天逾期金额
print(content.loc['n_overdue_7days_amt', 'JIN_JIE_DAO_LOAN'])
# 借入笔数
print(content.loc['n_borrow_cnt', 'JIN_JIE_DAO_LOAN'])
# 借入人数
print(content.loc['n_borrow_people_num', 'JIN_JIE_DAO_LOAN'])

