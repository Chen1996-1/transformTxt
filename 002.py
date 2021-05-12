import numpy as np


file_path = '111.txt'

file_arry = np.loadtxt(file_path, encoding='utf-8', dtype=str, delimiter=', ')

print(file_arry)

delete_row_file_arry = np.delete(file_arry, 0, axis=0)
delete_column_file_arry = np.delete(file_arry, 0, axis=1)
print(delete_row_file_arry)
print(delete_column_file_arry)

first_row = file_arry[0, :]

first_colum = file_arry[:, 0]


# test_row = 'a,b,c,d,e,f,g'.split(',')

# file_arry[0, :] = test_row

# print(file_arry)

# a = np.delete(file_arry, 3, axis=0)
# print(a)

# print(file_arry)



