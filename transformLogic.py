import numpy as np

class Methods():
	def __init__(self, narry, (de_line_num_str, de_col_num_str, in_line_num_str, in_col_num_str, merge_col_str, exchange_col_str, split_col_str)):
		self.narry = narry
		self.de_line_num_str= de_line_num_str 
		self.de_col_num_str= de_col_num_str 
		self.in_line_num_str = in_line_num_str
		self.in_col_num_str = in_col_num_str
		self.merge_col_str = merge_col_str
		self.exchange_col_str = exchange_col_str
		self.split_col_str = split_col_str

	def delete_line(self):
		if self.de_line_num_str:
			try:
				de_line_num = int(self.de_line_num_str)
				de_line_array = np.delete(self.narry, de_line_num, axis=0)
				return de_line_array
			except:
				print('delete_line Error')

	def delete_col(self):
		if self.de_col_num_str:
			try: 
				de_col_num = int(self.de_col_num_str)
				de_col_array = np.delet(self.narry, de_col_num, axis=1)
			except:
				print('delete_col Error')

	def insert_line(self):
		print('insert_line')

	def insert_col(self):
		pirnt('insert_col')

	def merge_col(self):
		col_list = self.merge_col_str.split('=>')[0].split(',')