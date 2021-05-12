'''
如何使用Menu button
'''
import tkinter
from tkinter import *
from tkinter import ttk, filedialog, messagebox

import shutil


import time
import os

this_year = time.localtime().tm_year

class MyGuiana():

	def __init__(self, master):
		self.master = master
		self.mywidget()
		self.log_file_opt = options = {}  
		options['defaultextension'] = '.LOG'  
		options['filetypes'] = [('LOG files', '.LOG'), ('其他文件', '.*'),]  
		options['initialfile'] = ''  
		options['parent'] = root  
		options['title'] = '选择LOG文件' 
		self.scriptfile_opt = options = {}
		options['defaultextension'] = '.scr'
		options['filetypes'] = [('脚本文件', '.scr'), ('其他文件', '.*')]
		options['initialfile'] = ''
		options['parent'] = root
		options['title'] = '选择保存脚本文件'

	def mywidget(self):
		menubar = Menu(self.master)
		# menubar.add_command(label = '选择模式')

		capability_menu = Menu(menubar, tearoff = False)

		menubar.add_cascade(label = '菜单', menu = capability_menu)

		capability_menu.add_command(label = 'Hypack版本转换', command = self.version_transform_widget)	
		capability_menu.add_separator()
		capability_menu.add_command(label = '航迹线脚本生成器', command = self.track_line_widget)

		if  os.path.exists(os.getcwd()+'\\setup.su'):
			capability_menu.add_command(label = '配置', command = self.set_up_dir_black)

		# capability_menu.add_separator()
		# capability_menu.add_command(label = '水深生成', command = self.water_value_widget)


		self.master.config(menu = menubar)

		self.mainFrame = Frame(self.master)
		self.secondFrame = Frame(self.master)
		self.thirdFrame = Frame(self.master)

		self.mainFrame.grid(row = 0, column = 0)
		self.secondFrame.grid(row = 1, column = 1)
		self.thirdFrame.grid(row = 2, column = 2)

		label = Label(self.mainFrame, text = '{}年身体健康\ngood good study, day day up！'.format(this_year), font = 600)
		label.grid()

	def set_up_dir_black(self):# 获取插入块路径的函数，未完成
		self.mainFrame.destroy()
		self.secondFrame.destroy()
		self.thirdFrame.destroy()



	def water_value_widget(self):
		'''水深页面'''
		self.mainFrame.destroy()
		self.secondFrame.destroy()
		self.thirdFrame.destroy()

		self.mainFrame = Frame(self.master)
		self.secondFrame = Frame(self.master)
		self.thirdFrame = Frame(self.master)

		self.mainFrame.grid(row = 0, column = 0)
		self.secondFrame.grid(row = 1, column = 1)
		self.thirdFrame.grid(row = 2, column = 2)


		self.select_file_button = Button(self.mainFrame, text = '选择.Log文件', command = self.open_log)
		self.select_file_button.grid(row = 0, column = 0, padx = 15, pady = 10)
		# Label(self.mainFrame, text = '       水深页面               ', font = 10).grid(row = 0, column = 1)


		self.water_deep_granularity_entry = Entry(self.secondFrame)
		self.water_deep_granularity_entry.grid(row = 1, column  = 1)
		self.water_deep_granularity_entry.insert(0, '间隔取点距离(m):')

		self.water_deep_scale_entry = Entry(self.secondFrame)
		self.water_deep_scale_entry.grid(row = 1, column = 2, padx =10)
		self.water_deep_scale_entry.insert(0, '比例尺 1：')

		self.adjust_tide_value_entry = Entry(self.secondFrame)
		self.adjust_tide_value_entry.grid(row = 2, column = 1,pady = 15 )
		self.adjust_tide_value_entry.insert(0, '潮汐改正值(m):')

		self.select_tide_button = Button(self.secondFrame, text = '选择潮汐文件', command = self.open_tide)
		self.select_tide_button.grid(row = 6, column = 1, ipadx = 15, pady = 10)

		Button(self.secondFrame, text = '选择脚本位置', command = self.save_script).grid(row = 6, column = 2, padx = 15, pady = 10, ipady = 1, ipadx = 5)
		Button(self.secondFrame, text = ' 确定 ', command =self.water_deep_deal_program).grid(row = 6, column = 3,pady = 10,padx = 10,ipady = 1, ipadx = 5)
		self.lastFrame = ttk.Progressbar(orien='horizontal',length = 500)
		self.lastFrame.grid(row = 3, column =0, columnspan = 8)	
		print('水深')

	def track_line_widget(self):
		'''航迹线页面'''

		self.mainFrame.destroy()
		self.secondFrame.destroy()
		self.thirdFrame.destroy()

		self.mainFrame = Frame(self.master)
		self.secondFrame = Frame(self.master)
		self.thirdFrame = Frame(self.master)

		self.mainFrame.grid(row = 0, column = 0)
		self.secondFrame.grid(row = 1, column = 1)
		self.thirdFrame.grid(row = 2, column = 2)


		self.select_file_button = Button(self.mainFrame, text = '选择.Log文件', command = self.open_log)
		self.select_file_button.grid(row = 0, column = 0, padx = 15, pady = 10)

		self.cV = tkinter.IntVar()
		# secondFrame = Frame(self.master)
		# secondFrame.grid(row = 1, column = 1)
		self.track_line_name_stlye = Checkbutton(self.secondFrame, variable = self.cV, text = '日期线号为线名', anchor = 'e', onvalue = 1, offvalue = 0)
		self.track_line_name_stlye.grid(row = 1,  column = 1, padx =20,  )

		self.track_line_granularity_entry = Entry(self.secondFrame)
		self.track_line_granularity_entry.grid(row = 1, column  = 2)
		self.track_line_granularity_entry.insert(0, '间隔取点数(0.5m):')

		self.track_line_scale_entry = Entry(self.secondFrame)
		self.track_line_scale_entry.grid(row = 3, column = 2)
		self.track_line_scale_entry.insert(0, '比例尺 1：')

		self.markId = tkinter.IntVar()
		self.track_line_mark_insert = Checkbutton(self.secondFrame, variable = self.markId, text = '是否要插入块', anchor = 'e', onvalue = 1, offvalue = 0)
		self.track_line_mark_insert.grid(row = 3, column = 1)

		Button(self.secondFrame, text = '选择脚本位置', command = self.save_script ).grid(row = 6, column = 2, padx = 15, pady = 10, ipady = 1, ipadx = 5)
		Button(self.secondFrame, text = ' 确定 ', command =self.track_line_deal_program).grid(row = 6, column = 5,pady = 10,padx = 10,ipady = 1, ipadx = 5)
		self.lastFrame = ttk.Progressbar(orien='horizontal',length = 500)
		self.lastFrame.grid(row = 3, column =0, columnspan = 8)		


		print('航迹线')

	def version_transform_widget(self):
		'''Hypack版本转换页面'''
		self.mainFrame.destroy()
		self.secondFrame.destroy()
		self.thirdFrame.destroy()
		
		self.mainFrame = Frame(self.master)
		self.secondFrame = Frame(self.master)
		self.thirdFrame = Frame(self.master)

		self.mainFrame.grid(row = 0, column = 0)
		self.secondFrame.grid(row = 1, column = 1)
		self.thirdFrame.grid(row = 2, column = 2)



		self.select_file_button = Button(self.mainFrame, text = '选择.Log文件', command = self.open_log)
		self.select_file_button.grid(row = 0, column = 0, padx = 15, pady = 10)

		Label(self.secondFrame, text = '生成文件的标识符：').grid(row = 0, column = 1)
		self.one = Entry(self.secondFrame,)
		self.one.grid(row = 0, column = 2, pady = 3)
		# Label(one, text= '@@@@@').grid(sticky = NW)


		Label(self.secondFrame, text = '初始文件的标识符：').grid(row = 2, column = 1)
		self.two = Entry(self.secondFrame,)
		self.two.grid(row = 2, column = 2, pady = 3)
		# Label(two, text = 'EOH   ').grid(sticky = NW)

		Button(self.secondFrame, text = ' 确定 ', command =self.version_transform_deal_program).grid(row = 6, column = 5,pady = 10,padx = 10,ipady = 1, ipadx = 5)

		self.lastFrame = ttk.Progressbar(orien='horizontal',length = 500)
		self.lastFrame.grid(row = 3, column =0, columnspan = 8)
		print('版本转换')




	def open_log(self, trail_count=2):

		'''打开log文件，获取文件路径等'''
		print('open_log')

	def open_tide(self):
		'''添加潮汐文件'''
		print('open_tide')
	def save_script(self, trail_count=2):
		'''保存到脚本文件'''
		print('save_script')
	
	def version_transform_deal_program(self):
		'''版本转换工具开始执行'''
		print('version_transform_deal_program')
		


	def track_line_deal_program(self):
		'''航迹线'''
		print('track_line_function')
		


	def water_deep_deal_program(self):
		
		# del resultfile	
		print('water_deep_deal_program')

date_end = '2022-12-31'
if __name__ == '__main__':
	if time.strptime(date_end,'%Y-%m-%d').__ge__(time.localtime()):
		pass
	else:
		raise NameError
	root = Tk()
	root.resizable(0,0)
	root.title('Hypack单波束小工具')
	MyGuiana(root)
	root.mainloop()