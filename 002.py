import numpy as np


file_path = '111.txt'

file_arry = np.loadtxt(file_path, encoding='utf-8', dtype=str, delimiter=', ')

print(file_arry, end='\n ############\n')

i = 5 
delete_row_file_arry = np.delete(file_arry, i, axis=0)
delete_column_file_arry = np.delete(file_arry, 0, axis=1)


first_row = file_arry[i, :]
j = 3

j_row = file_arry[j, :]

d_i_j_arry = np.delete(file_arry, [i,j], axis=0)


print(delete_row_file_arry, end='\n*************\n')
print(first_row, end="\ndddddddddddddddddd\n")

merge_=np.frompyfunc(lambda x,y:x+y,2,1)

merge_i_j = merge_(first_row, j_row)

a = np.insert(d_i_j_arry, i-1,  merge_i_j, axis=0)

first_row_list = list(first_row)
print(first_row_list)

child_list = [i.split('-') for i in first_row_list]

print(np.array(child_list))



