# -*- coding: utf-8 -*-
# author：Super.Shen
import os
import shutil
# path = 'C:\\Users\Administrator\Desktop\\text'
path = 'C:\\Users\Administrator\Documents\WeChat Files\shenyuanji9339\Files'
new_path = 'C:\\Users\Administrator\Desktop'

from Daily.Func import nian, yue, ri_now
if len(yue) < 2:
    yue = '0' + yue
if len(ri_now) < 2:
    ri_now = '0' + ri_now

alllist = os.listdir(path)
for i in alllist:
    if len(i.split('-')) < 3:
        print('文件名称有问题，请检查！')
        exit()


    else:
        # 产生信号
        signal = i.split('-')[0]
        name = i.split('-')[1]

        ziyuan = input('\n{} -- {} 需要资源\n\n请输入你的资源标记： \n'.format(signal, name))

        old = path + '\\'+i
        new = new_path+'\\'+i
        shutil.move(old, new)

        if signal == '电销':
            old2 = 'D:\Super\电话资源分配模板\电销-姓名-20180620.xlsx'
            new2 = new_path + '\\' + signal + '-' + name + '-' + nian + yue + ri_now + '-' + ziyuan + '.xlsx'
            shutil.copyfile(old2, new2)
        elif signal == '风控':
            old2 = 'D:\Super\电话资源分配模板\风控-姓名-20180620.xlsx'
            new2 = new_path + '\\' + signal + '-' + name + '-' + nian + yue + ri_now + '-' + ziyuan + '.xlsx'
            shutil.copyfile(old2, new2)
