from re import search
import numpy as np
import tkinter
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from tkinter.ttk import Treeview
import time

from numpy.lib.function_base import delete, piecewise
from numpy.lib.type_check import typename
from numpy.testing._private.utils import print_assert_equal

l = [
  ['a','b','c','d','e-f'],
  ['A','B','C','D','E-E'],
  ['1','2','3','4', '5-5']
]
class ArryDeal():

  def __init__(self, list_arr):
    print('ArryDeal')
    '''传入一个列表,实例化'''
    if isinstance(list_arr, list):
      self.arr= np.array(list_arr)
    else:
      self.arr = list_arr

  def delete_columns(self, col_str):
    col__num_list = [int(i) for i in col_str.split(',')]
    delete_col_arr = np.delete(self.arr, col__num_list, axis=1)
    print(delete_col_arr)
    print(self.arr)
    return delete_col_arr
  
  def delete_rows(self, row_str):
    row_num_list = [int(i) for i in row_str.split(',')]
    delete_row_arr = np.delete(self.arr, row_num_list, axis=0)
    print(delete_row_arr)
    print(self.arr)
    return delete_row_arr

  def merge_col(self, col_str):
    column_num_list = [int(i) for i in col_str.split(',')]
    merge_index = column_num_list[0]
    merge_arr = self.arr[:, merge_index]
    merge = np.frompyfunc(lambda x,y : x+y, 2, 1)
    for i in range(1,len(column_num_list)):
      merge_arr = merge(merge_arr, self.arr[:, column_num_list[i]])
    
    merge_col_arr =np.insert(self.delete_columns(col_str=col_str), merge_index, merge_arr, axis=1) 
    print(merge_col_arr)
    print(self.arr)
    return merge_col_arr
  
  def exchange_col(self, col_str):
    column_num_list = [int(i) for i in col_str.split(',')]
    one = column_num_list[0]
    two = column_num_list[1]
    delete_col_arr = self.delete_columns(col_str)
    insert_two_to_one_arr = np.insert(delete_col_arr, one, self.arr[:, two], axis=1)
    exchange_col_arr = np.insert(insert_two_to_one_arr, two, self.arr[:, one], axis=1)

    print(exchange_col_arr)
    print(self.arr)
    return exchange_col_arr

  def split_col(self, col_str):
    column_delimiter= col_str.split('|')
    column_num = int(column_delimiter[0])
    delimiter = column_delimiter[1]
    before_arr,column_arr, after_arr = np.hsplit(self.arr, (column_num, column_num+1))
    column_list = column_arr.tolist()
    child_cols_arr= np.array([i[0].split(delimiter) for i in column_list])
    split_col_arr = np.hstack((before_arr, child_cols_arr, after_arr))

    print(child_cols_arr)
    print(split_col_arr)
    print(self.arr)
    return split_col_arr



class TkinterModel():

  def __init__(self, window): 
    print('TkinterModel')
    self.window = window
    self.rander_menu()
    self.log_file_opt = options = {}  
    options['defaultextension'] = '.txt'  
    options['filetypes'] = [('txt文件', '.txt'),('CSV文件', '.csv'), ('其他文件', '.*'),]  
		# options['initialdir'] = 'C:\\'  
    options['initialfile'] = ''  
    options['parent'] = self.window 
    options['title'] = '选择文件' 

  def readSetup(self):
    f = open('setup.su', 'r', encoding='utf-8')
    data = f.read()
    f.close()
    data = eval(data)
    self.default_delimiter_str = data['delimiter']
    self.default_delete_line_str = data['delete_line']
    self.default_insert_line_str = data['insert_line']
    self.default_delete_col_str = data['delete_col']
    self.default_insert_col_str = data['insert_col']
    self.default_exchange_col_str = data['exchange_col']
    self.default_merge_col_str = data['merge_col']
    self.default_split_col_str = data['split_col']

  def writeSetup(self, data):
    data = {
    'delimiter': '',
    'delete_line': '',
    'insert_line': '',
    'delete_col': '',
    'insert_col': '',
    'exchange_col': '',
    'merge_col': '',
    'split_col': ''
    }
    data['delimiter'] = self.current_delimiter_str
    data['delete_line'] = self.current_delete_line_str
    data['insert_line'] = self.current_insert_line_str
    data['delete_col'] = self.current_delete_col_str
    data['insert_col'] = self.current_insert_col_str
    data['exchange_col'] = self.current_exchange_col_str
    data['merge_col'] = self.current_merge_col_str
    data['split_col'] = self.current_split_col_str
    str_data = str(data)

    f = open('setup.su', 'w', encoding='utf-8')
    f.write(str_data)
    f.close()

  def get_args(self):
    print('get_args')
    self.current_delimiter_str = self.delimiter_entry.get()
    self.current_delete_line_str = self.delete_line_entry.get()
    self.current_delete_col_str = self.delete_col_entry.get()
    self.current_exchange_col_str = self.exchange_col_entry.get()
    self.current_merge_col_str = self.merge_col_entry.get()
    self.current_split_col_str = self.split_col_entry.get()

  def rander_table(self, file_arry):
    rows_count, cols_count = file_arry.shape
    rows = tuple(i for i in range(rows_count)) 
    cols = tuple(i for i in range(cols_count))
    ybar = Scrollbar(self.table, orient='vertical')      #竖直滚动条 
    xbar = Scrollbar(self.table, orient='horizontal')
    tree = Treeview(self.table, show='headings', columns=cols, yscrollcommand=ybar.set, xscrollcommand=xbar.set)

    ybar['command'] = tree.yview      
    xbar['command'] = tree.xview			
    for col in cols:
      tree.heading(col,text=col)             #行标题
      tree.column(col,width=80,anchor='c')   #每一行的宽度,'w'意思为靠右

    #插入数据
    for i in range(rows_count):
      l = file_arry[i, :]
      t = (i,)+tuple(l)
      print(t)
      tree.insert("","end",values=t)

    ybar.pack(side='right',fill='y')		#pack方案
    xbar.pack(side='bottom', fill='x')
    tree.pack(fill='both', expand=True)
    self.table.pack()	

  def write_to_new(self, arr):
    print('write_to_new')
    file_name = self.new_file_path
    np.savetxt(file_name, arr, fmt='%s', delimiter=self.current_delimiter_str)


  def deal(self, arr):
    print('deal')
    arr_model = ArryDeal(arr)
    if self.current_delete_line_str:
      arr_delete_line = arr_model.delete_rows(self.current_delete_line_str)
      self.rander_table(arr_delete_line)
    if self.current_delete_col_str:
      arr_delete_col = arr_model.delete_columns(self.current_delete_col_str)
      self.rander_table(arr_delete_col)
    if self.current_exchange_col_str:
      arr_exchange_col = arr_model.exchange_col(self.current_exchange_col_str)
      self.rander_table(arr_exchange_col)
    if self.current_merge_col_str:
      arr_merge_col = arr_model.merge_col(self.current_merge_col_str)
      self.rander_table(arr_merge_col)
    if self.current_split_col_str:
      arr_split_col = arr_model.split_col(self.current_split_col_str)
      self.rander_table(arr_split_col)


  def openSingleFile(self, trail_count=2):
    print('openSingleFIle')
    '''打开log文件，获取文件路径等'''
    while trail_count:
      file_path = filedialog.askopenfilename(**self.log_file_opt)
      if file_path:
        self.get_args()
        file_leng_name= file_path.split('/')[-1]
        file_name, file_type = file_leng_name.split('.')
        file_leng_name_new = 't_' + file_name +file_type
        self.new_file_path = file_path.replace(file_leng_name, file_leng_name_new)
        file_arry = np.loadtxt(file_path, encoding='utf-8', dtype=str, delimiter=self.current_delimiter_str)
        self.rander_table(file_arry)
        self.deal(file_arry)

      else:
        tkinter.messagebox.showinfo(title = '提示', message = '没有选择文件')
        self.openSingleFile(trail_count-1)
    tkinter.messagebox.showinfo(title = '提示', message = '暂不选择LOG文件')

    

  def openMutilFiles(self):
    print('openMutilFiles')

  def rander_menu(self):
    print('rander_menu')
    self.readSetup()
    menubar = Menu(self.window)
    capability_menu = Menu(menubar, tearoff = False)
    menubar.add_cascade(label = '菜单', menu = capability_menu)
    capability_menu.add_command(label = '打开单个文件', command=self.openSingleFile)
    capability_menu.add_command(label='打开多个文件', command=self.openMutilFiles )


    self.window.config(menu=menubar)
    self.window.geometry('600x450')
    self.table = Frame(self.window)
    programFrame = Frame(self.window)

    delete_line = Label(programFrame, text="删除行").grid(row=0, column=0)
    self.delete_line_entry = Entry(programFrame, width=5, textvariable=self.default_delete_line_str)
    self.delete_line_entry.grid(row=0, column=1)
    self.delete_line_entry.insert(0, self.default_delete_line_str)


    delete_col= Label(programFrame, text="删除列").grid(row=0, column=4)
    self.delete_col_entry= Entry(programFrame, width=5)
    self.delete_col_entry.grid(row=0, column=5)
    self.delete_col_entry.insert(0, self.default_delete_col_str)

    delimiter_label = Label(programFrame, text="分隔符").grid(row=0, column=8)
    self.delimiter_entry = Entry(programFrame, width=5)
    self.delimiter_entry.grid(row=0, column=9)
    self.delimiter_entry.insert(0, self.default_delimiter_str)

    exchange_col= Label(programFrame, text="交换列").grid(row=1, column=0, pady=10)
    self.exchange_col_entry = Entry(programFrame, width=10)
    self.exchange_col_entry.grid(row=1, column=1, pady=10)
    self.exchange_col_entry.insert(0, self.default_exchange_col_str)

    merge_col= Label(programFrame, text="合并列").grid(row=1, column=2, pady=10)
    self.merge_col_entry = Entry(programFrame, width=10)
    self.merge_col_entry.grid(row=1, column=3, pady=10)
    self.merge_col_entry.insert(0, self.default_merge_col_str)

    split_col= Label(programFrame, text="拆分列").grid(row=1, column=4, pady=10)
    self.split_col_entry = Entry(programFrame, width=10)
    self.split_col_entry.grid(row=1, column=5, pady=10)
    self.split_col_entry.insert(0, self.default_split_col_str)

    submit_button = Button(programFrame, text="保存参数", command=self.writeSetup)
    submit_button.grid(row=1, column=6, ipadx=15, columnspan=8)

    run_deal_button = Button(programFrame, text='开始', command=self.deal)
    run_deal_button.grid(row=2, column=1, ipadx=20, padx=30)

    programFrame.pack()

window = Tk()
TkinterModel(window)
window.mainloop()



















a = ArryDeal(l)
a.split_col('4|-')

# a.delete_columns('1')
# a.delete_rows('1,2')
# a.merge_col('0,1,3')
# a.exchange_col('2,3')
