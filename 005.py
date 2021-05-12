from tkinter import *
from tkinter.ttk import Treeview
import numpy as np



file_path = '111.txt'

file_arry = np.loadtxt(file_path, encoding='utf-8', dtype=str, delimiter=', ')

rows_count, cols_count = file_arry.shape

window=Tk()

menubar = Menu(window)
capability_menu = Menu(menubar, tearoff = False)
menubar.add_cascade(label = '菜单', menu = capability_menu)
capability_menu.add_command(label = '打开单个文件')	
capability_menu.add_command(label='打开多个文件')


window.config(menu=menubar)
window.geometry('500x450')
table = Frame(window)
programFrame = Frame(window)



rows = tuple(i for i in range(rows_count)) 
cols = tuple(i for i in range(cols_count))

ybar = Scrollbar(table, orient='vertical')      #竖直滚动条 
xbar = Scrollbar(table, orient='horizontal')
tree = Treeview(table, show='headings', columns=cols, yscrollcommand=ybar.set, xscrollcommand=xbar.set)

ybar['command'] = tree.yview      
xbar['command'] = tree.xview

delete_line = Label(programFrame, text="删除行").grid(row=0, column=0)
delete_line_entry = Entry(programFrame, width=5).grid(row=0, column=1)

insert_line= Label(programFrame, text="插入行").grid(row=0, column=2)
insert_line_entry = Entry(programFrame, width=5).grid(row=0, column=3)

delete_col= Label(programFrame, text="删除列").grid(row=0, column=4)
delete_col_entry= Entry(programFrame, width=5).grid(row=0, column=5)

insert_col= Label(programFrame, text="插入列").grid(row=0, column=6)
insert_col_entry = Entry(programFrame, width=5).grid(row=0, column=7)

exchange_col= Label(programFrame, text="交换列").grid(row=1, column=0, pady=10)
exchange_col_entry = Entry(programFrame, width=10).grid(row=1, column=1, pady=10)

merge_col= Label(programFrame, text="合并列").grid(row=1, column=2, pady=10)
merge_col_entry = Entry(programFrame, width=10).grid(row=1, column=3, pady=10)

split_col= Label(programFrame, text="拆分列").grid(row=1, column=4, pady=10)
split_col_entry = Entry(programFrame, width=10).grid(row=1, column=5, pady=10)

submit_button = Button(programFrame, text="提交").grid(row=1, column=6, ipadx=15, columnspan=8)


#表头设置
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
table.pack()
programFrame.pack(pady=20)
# submit_button = Button(window, text="提交").pack(ipadx=50, pady=30)


window.mainloop()



def get_all_args(delete_line_entry, delete_col_entry, insert_col_entry, insert_line_entry, exchange_col_entry, merge_col_entry, split_col_entry):
	delete_line_list = list(delete_line_entry.get())
	delete_col_list= list(delete_col_entry.get())
	insert_col_list= list(insert_col_entry.get())
	exchange_col_list = list(exchange_col.get())
	merge_col_list = list(merge_col_entry.get())
	split_col_list = list(split_col_entry.get())


