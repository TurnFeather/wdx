# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from openpyxl import Workbook
import os
import subprocess

def read_process_cpu_info():
    top_info = subprocess.Popen(["top","-o","%CPU", "-n", "1"], stdout=subprocess.PIPE)
    out, err = top_info.communicate()

    # output info get from console has many unicode escape character ,such as \x1b(B\x1b[m\x1b[39;49m\x1b[K\n\x1b(B\x1b[m
    # use decode('unicode-escape') to process

    out_info = out.decode('unicode-escape')
    lines = []
    lines = out_info.split('\n')
    newstr = ''
    count = 6
    while count < 13:
        newstr = newstr + lines[count] + '\n'
        count = count + 1
    return newstr
#这里可能多个文件
def read_log(path_prefix,*args):
    for file_name in args:
        file_path = os.path.join(path_prefix,os.sep,file_name)
#拿到稳定性模版
#wb = load_workbook(r"C:\Users\yuron\Desktop\python_test.xlsx",False)
#从文件中读值

#发送邮件

#在保存值的过程中，调用此python脚本，来保存成需要发送的excel文件

# sheet = wb.get_sheet_by_name("Sheet1")
# sheet['E5']=40
# wb.save(r"C:\Users\yuron\Desktop\python_test.xlsx")

if __name__ == "__main__":
    print(read_process_cpu_info())