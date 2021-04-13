import os
from excel_utils.excel_write import write_to_excel, append_to_excel

a = [{'姓名': 'zs', 'age': 30}, {'姓名': '李四', 'age': 50}]

# 写入excel表格
fileName = 'test.xls'
if not os.path.exists(fileName):
    write_to_excel(a, fileName)
else:
    append_to_excel(a, fileName)
