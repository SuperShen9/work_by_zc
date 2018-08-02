# -*- coding: utf-8 -*-
# author：Super.Shen

import pandas as pd
import datetime
pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

df = pd.read_hdf('D:\Super\database\data.h5', key='data')

# #按 名称 提取资源
# df = df[df['资源来源'].apply(lambda x:x[:2]) == '机猫']
# df.to_excel('C:\\Users\Administrator\Desktop\每日核对数据.xlsx', index=False)
# exit()

# 查看资源比例
# for x,y in df.groupby('资源来源'):
#     print(x)
# print(df.groupby('资源来源').size())
# exit()

# df.to_hdf('D:\Super\database\data.h5', key='data', mode='a')

rizhi = pd.read_excel('D:\Super\资源汇总代码run\日志.xlsx')
rz_add = pd.DataFrame()

or_count = df.shape[0]
df_add = pd.read_excel('D:\Super\资源汇总代码run\Feedback_Data.xlsx')
add_count = df_add.shape[0]

df = df.append(df_add, ignore_index=True)
df.drop_duplicates(keep='first', inplace=True)

rz_add.loc[0, '代码运行时间'] = str(datetime.datetime.now())[:19]
rz_add.loc[0, '起始数据量'] = or_count
rz_add.loc[0, '加入数据量'] = df.shape[0]-or_count
rz_add.loc[0, '数据总量'] = df.shape[0]
rizhi = rizhi.append(rz_add)

# 下次验证之后删除
rizhi = rizhi.reset_index(drop=True)

all_count = df.shape[0]

if df.shape[1] == 9:
    print('\n数据库新增数据量：{}条'.format(all_count-or_count))
    print('\n{}条数据被去重'.format(add_count - (all_count - or_count)))
    df.to_hdf('D:\Super\database\data.h5', key='data', mode='a')
    rizhi.to_excel('D:\Super\资源汇总代码run\日志.xlsx')
else:
    print('\n数据列有问题，请仔细核对!')

exit()

# # 标准数据列
# df2 = pd.read_excel('D:\Super\database\列名更新.xlsx')
# df=pd.merge(left=df,right=df2,on='资源来源',how='left',sort=True)
# df['资源来源'] = df['Flag']
# df=df[df.columns[:-1]]
# df.to_hdf('D:\Super\database\data.h5', key='data')
# exit()


# # 统计接通率/需求率
# i = 0
# df1 = pd.DataFrame()
# for x, y in df.groupby(['资源来源']):
#     df1.loc[i, '资源名称'] = x
#     df1.loc[i, '电话数量'] = y['资源来源'].count()
#     df1.loc[i, '接通率'] = str(int((y[y['接通率'] == '接通']['接通率'].count() / y['接通率'].count()) * 100))+'%'
#     df1.loc[i, '需求率'] = str(int((y[y['需求率'] == '需要']['需求率'].count() / y['需求率'].count()) * 100))+'%'
#     i += 1
# df1.to_excel('C:\\Users\Administrator\Desktop\\总数据统计.xlsx')


# # 重置资源
# df=df[df['资源来源']!='还']
# df.to_hdf('D:\Super\database\data.h5', key='data')
# exit()