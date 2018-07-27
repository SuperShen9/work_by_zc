# -*- coding: utf-8 -*-
# author：Super.Shen
import os, openpyxl


# wb = openpyxl.load_workbook('C:\\Users\Administrator\Desktop\电销1.xlsx')
# sheet = wb.active
# hang = sheet.max_row
# lie = sheet.max_column
# sheet['A2']=1
#
# wb.save('C:\\Users\Administrator\Desktop\\1.xlsx')

import datetime
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# print(datetime.datetime.now().strftime('%H'))
# exit()


hour = datetime.datetime.now().strftime('%H')
# print(type(hour))
print(int(hour)>7)

# print(18>13)