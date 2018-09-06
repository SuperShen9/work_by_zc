# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

# 读取电销汇总
df = pd.read_excel('C:\\Users\Administrator\Desktop\Feedback_Data.xlsx')
# 读取申请数据
df2 = pd.read_excel('D:\Super\shudang\\shenqing.xlsx')
# 读取下单数据
df3 = pd.read_excel('D:\Super\shudang\\xiadan.xlsx')
# 读取数据
df4 = pd.read_excel('D:\Super\shudang\\jujue.xlsx')

# 更改固定来源
df['资源来源'] = '渠道A'
# 添加申请列
df2['申请率'] = '申请'
# 重命名- 申请 -手机列--用于merge
df2.rename(columns={'用户手机号': '手机号'}, inplace=True)

# 添加下单列
df3['下单率'] = '下单'
# 重命名- 下单 -手机列--用于merge
df3.rename(columns={'用户手机号': '手机号'}, inplace=True)

# 添加拒绝列
df4['拒绝率'] = '拒绝'
# 重命名- 拒绝 -手机列--用于merge
df4.rename(columns={'用户手机号': '手机号'}, inplace=True)

# 合并申请数据
df = pd.merge(left=df, right=df2, on='手机号', how='left')
# 合并下单数据
df = pd.merge(left=df, right=df3, on='手机号', how='left')
# 合并拒绝数据
df = pd.merge(left=df, right=df4, on='手机号', how='left')

# 填充未匹配到的数据
df['申请率'] = df['申请率'].fillna(value='未申请')
df['下单率'] = df['下单率'].fillna(value='未下单')
df['拒绝率'] = df['拒绝率'].fillna(value='未拒绝')

# 筛选需要的列
df = df[['资源来源', '资源发送时间', '手机号', '部门', '姓名', '数据反馈', '数据反馈2', '接通率', '需求率', '申请率', '拒绝率', '下单率']]
# 导出数据
df.to_excel('C:\\Users\Administrator\Desktop\Feedback.xlsx', index=False)
