#-*- coding:utf-8 -*-

import xlrd
import xlwt

data_read = xlrd.open_workbook(u'站点月份数据.xlsx')
data_write = xlwt.Workbook()

# 修改下面两个地方来获取不同的sheet数据，然后生成不同的数据
table_read = data_read.sheets()[6]
table_write = data_write.add_sheet(u'七月份日均数据', cell_overwrite_ok=True)

table_write.write(0, 0, 'date')
table_write.write(0, 1, 'pv')
table_write.write(0, 2, 'uv')

nrows = table_read.nrows

data_list_date=[]
data_list_pv={}
data_list_uv={}

func = lambda x:x.value    

data_list_date.extend(map(func,table_read.col(1)))

data_list_date = data_list_date[1:]

func3 = lambda x,y:x if y in x else x + [y]

data_list_date = reduce(func3, [[], ] + data_list_date)

for index, item in enumerate(data_list_date):
	sum_pv_number = 0
	sum_uv_number = 0
	for row in range(nrows):
		if table_read.cell(row, 1).value == item:
			sum_pv_number += table_read.cell(row, 2).value
			sum_uv_number += table_read.cell(row, 3).value
	table_write.write(index+1, 0, item)
	table_write.write(index+1, 1, sum_pv_number)
	table_write.write(index+1, 2, sum_uv_number)

data_write.save('/Users/yangli/Desktop/test7.xls')
