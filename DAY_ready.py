# -*- coding: utf-8 -*-
# author：Super.Shen

import os
from Week_Report.Func import nian,yue,ri_now
if len(yue) < 2:
    yue = '0' + yue
if len(ri_now) < 2:
    ri_now = '0' + ri_now

# file1 = 'C:\\Users\Administrator\Desktop\\{}{}{} a'.format(nian, yue, ri_now)
# file2 = 'C:\\Users\Administrator\Desktop\\{}{}{} b'.format(nian, yue, ri_now)
# file3 = 'C:\\Users\Administrator\Desktop\\{}{}{} c'.format(nian, yue, ri_now)

file1 = 'C:\\Users\Administrator\Desktop\\{}{}{} 分数据'.format(nian, yue, ri_now)
file2 = 'C:\\Users\Administrator\Desktop\\{}{}{} 数据收集'.format(nian, yue, ri_now)
file3 = 'C:\\Users\Administrator\Desktop\\{}{}{} 工作量'.format(nian, yue, ri_now)
file6 = 'C:\\Users\Administrator\Desktop\\{}{}{} 员工报告'.format(nian, yue, ri_now)
file7 = 'C:\\Users\Administrator\Desktop\\{}{}{} 现金贷汇总'.format(nian, yue, ri_now)
# file4 = 'C:\\Users\Administrator\Desktop\\巧玲 {}{}'.format(yue, ri_now)
# file5 = 'C:\\Users\Administrator\Desktop\\陈磊 {}{}'.format(yue, ri_now)

list1 = [file1, file2, file3,  file6,  file7]
# file4, file5,

for i in list1:
    if os.path.exists(i):
        print('\n已创建文件！')
    else:
        os.mkdir(i)