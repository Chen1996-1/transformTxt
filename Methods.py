import numpy as np

class Methods():
	def __init__(self, narry, str_done):
		self.narry = narry
		self.str_done = str_done
		# self.de_line_num_str= de_line_num_str 
		# self.de_col_num_str= de_col_num_str 
		# self.in_line_num_str = in_line_num_str
		# self.in_col_num_str = in_col_num_str
		# self.merge_col_str = merge_col_str
		# self.exchange_col_str = exchange_col_str
		# self.split_col_str = split_col_str

	def delete_line(self):
		if self.str_done:
			try:
				de_line_num = int(self.str_done)
				de_line_array = np.delete(self.narry, de_line_num, axis=0)
				return de_line_array
			except:
				print('delete_line Error')

	def delete_col(self):
		if self.str_done:
			try: 
				de_col_num = int(self.str_done)
				de_col_array = np.delet(self.narry, de_col_num, axis=1)
			except:
				print('delete_col Error')

	def insert_line(self):
		print('insert_line')

	def insert_col(self):
		pirnt('insert_col')

	def merge_col(self):
		arg_col_list = self.str_done.split('=>')
		col_list = arg_col_list[0].split(',')
		col_merge_int = int(arg_col_list[-1])
		col_list_int = [int(i) for i in col_list].sort()

		de_col_arry = np.delete(narry, col_list_int, axis=1)

		merge = np.frompyfunc(lambda x,y : x+y, 2, 1)

		col_count = len(col_list_int)
		col = narry[:, col_list_int[0]]
		for i in range(1, col_count):
			col = merge(col, narry[:, col_list_int[i]])

		merge_arry = np.insert(de_col_arry, col_list_int[0], col, axis=1)

		return merge_arry


	def exchange_col(self):
		arg_col_list = self.str_done.split('<>')

		a = int(arg_col_list[0])
		b = int(arg_col_list[1])

		a_col = self.narry[:, a]
		b_col = self.narry[:, b]

		delete_arr_a_b = np.delete(narry, [a,b], axis=1)

		inser_a = np.insert(delete_arr_a_b, a, b_col, axis=1)
		exhcange_arr = np.insert(delete_arr_a_b, b, a_col, axis=1)

		return exhcange_arr

	def splic_col(self):
		arg_col_list = self.str_done.split('=<')

		father_col_int = int(arg_col_list[0])
		tirems_str =  arg_col_list[1]

		father_col = self.narry[:, father_col_int]
		delete_father_arry = np.delete(narry, father_col_int, axis=1)

		father_col_list = list(father_col)

		childs_col_list = [i.split(tirems_str) for i in father_col_list]

		childs_col = np.array(childs_col_list)

		splic_arr = np.insert(delete_father_arry, father_col_int, childs_col, axis=1)

		return splic_arr




















