import tkinter
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from tkinter.ttk import Treeview
import numpy as np

from Methods import Methods


class AppliGui():

	def __init__(self, window):
		self.window = window
		self.Gui() 
		self.log_file_opt = options = {}  
		options['defaultextension'] = '.txt'  
		options['filetypes'] = [('txt文件', '.txt'),('CSV文件', '.csv'), ('其他文件', '.*'),]  
		# options['initialdir'] = 'C:\\'  
		options['initialfile'] = ''  
		options['parent'] = window 
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
		return (self.default_delimiter_str, self.default_delete_line_str, self.default_insert_line_str, self.default_delete_col_str, self.default_insert_col_str, self.default_exchange_col_str, self.default_merge_col_str, self.default_split_col_str)


	def writeSetup(self, data):
		f = open('setup.su', 'w', encoding='utf-8')
		f.write(data)
		f.close()

	def get_args(self):
		self.current_delimiter_str = self.delimiter_entry.get()
		self.current_delete_line_str = self.delete_line_entry.get()
		self.current_insert_line_str = self.insert_line_entry.get()
		self.current_delete_col_str = self.delete_col_entry.get()
		self.current_insert_col_str = self.insert_col_entry.get()
		self.current_exchange_col_str = self.exchange_col_entry.get()
		self.current_merge_col_str = self.merge_col_entry.get()
		self.current_split_col_str = self.split_col_entry.get()
		
		data = {
		'delimiter': ', ',
		'delete_line': '2',
		'insert_line': '2',
		'delete_col': '3',
		'insert_col': '4',
		'exchange_col': '5',
		'merge_col': '6',
		'split_col': '7'
		}
		data['delimiter'] = self.current_delimiter_str
		data['delete_line'] = self.current_delete_line_str
		data['insert_line'] = self.current_insert_line_str
		data['delete_col'] = self.current_delete_col_str
		data['insert_col'] = self.current_insert_col_str
		data['exchange_col'] = self.current_exchange_col_str
		data['merge_col'] = self.current_merge_col_str
		data['split_col'] = self.current_split_col_str
		self.writeSetup(str(data))

		return  (self.current_delimiter_str,)

	def openSingleFile(self, trail_count=2):
		'''打开log文件，获取文件路径等'''
		while trail_count:
			file_path = filedialog.askopenfilename(**self.log_file_opt)
			if file_path:
				self.get_args()
				file_leng_name= file_path.split('/')[-1]
				file_name, file_type = file_leng_name.split('.')
				file_leng_name_new = 't_' + file_name +file_type
				new_file_path = file_path.replace(file_leng_name, file_leng_name_new)

				file_arry = np.loadtxt(file_path, encoding='utf-8', dtype=str, delimiter=self.current_delimiter_str)
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

			else:
				tkinter.messagebox.showinfo(title = '提示', message = '没有选择文件')
				self.openSingleFile(trail_count-1)

			print('open_log')
			return None

		tkinter.messagebox.showinfo(title = '提示', message = '暂不选择LOG文件')

	def openMutilFiles(self):
		pass




	def Gui(self):
		menubar = Menu(self.window)
		capability_menu = Menu(menubar, tearoff = False)
		menubar.add_cascade(label = '菜单', menu = capability_menu)
		capability_menu.add_command(label = '打开单个文件', command=self.openSingleFile)
		capability_menu.add_command(label='打开多个文件', command=self.openMutilFiles )

		default_delimiter_str, default_delete_line_str, default_insert_line_str, default_delete_col_str, default_insert_col_str, default_exchange_col_str, default_merge_col_str, default_split_col_str = self.readSetup()

		window.config(menu=menubar)
		window.geometry('600x450')
		self.table = Frame(self.window)
		programFrame = Frame(self.window)

		delete_line = Label(programFrame, text="删除行").grid(row=0, column=0)
		self.delete_line_entry = Entry(programFrame, width=5, textvariable=default_delete_line_str)
		self.delete_line_entry.grid(row=0, column=1)
		self.delete_line_entry.insert(0, default_delete_line_str)

		insert_line= Label(programFrame, text="插入行").grid(row=0, column=2)
		self.insert_line_entry = Entry(programFrame, width=5)
		self.insert_line_entry.grid(row=0, column=3)
		self.insert_line_entry.insert(0, default_insert_line_str)

		delete_col= Label(programFrame, text="删除列").grid(row=0, column=4)
		self.delete_col_entry= Entry(programFrame, width=5)
		self.delete_col_entry.grid(row=0, column=5)
		self.delete_col_entry.insert(0, default_delete_col_str)

		insert_col= Label(programFrame, text="插入列").grid(row=0, column=6)
		self.insert_col_entry = Entry(programFrame, width=5)
		self.insert_col_entry.grid(row=0, column=7)
		self.insert_col_entry.insert(0, default_insert_col_str)

		delimiter_label = Label(programFrame, text="分隔符").grid(row=0, column=8)
		self.delimiter_entry = Entry(programFrame, width=5)
		self.delimiter_entry.grid(row=0, column=9)
		self.delimiter_entry.insert(0, default_delimiter_str)

		exchange_col= Label(programFrame, text="交换列").grid(row=1, column=0, pady=10)
		self.exchange_col_entry = Entry(programFrame, width=10)
		self.exchange_col_entry.grid(row=1, column=1, pady=10)
		self.exchange_col_entry.insert(0, default_exchange_col_str)

		merge_col= Label(programFrame, text="合并列").grid(row=1, column=2, pady=10)
		self.merge_col_entry = Entry(programFrame, width=10)
		self.merge_col_entry.grid(row=1, column=3, pady=10)
		self.merge_col_entry.insert(0, default_merge_col_str)

		split_col= Label(programFrame, text="拆分列").grid(row=1, column=4, pady=10)
		self.split_col_entry = Entry(programFrame, width=10)
		self.split_col_entry.grid(row=1, column=5, pady=10)
		self.split_col_entry.insert(0, default_split_col_str)

		submit_button = Button(programFrame, text="提交", command=self.get_args)
		submit_button.grid(row=1, column=6, ipadx=15, columnspan=8)

		programFrame.pack()

		return (self.delete_line_entry, self.delete_col_entry, self.insert_line_entry, self.insert_col_entry, self.split_col_entry, self.merge_col_entry, self.exchange_col_entry)




window= Tk()
AppliGui(window)
window.mainloop()