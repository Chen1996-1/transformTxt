file_path = '111.txt'
file_leng_name= file_path.split('/')[-1]
file_name, file_type = file_leng_name.split('.')
file_leng_name_new = 't_' + file_name +file_type
new_file_path = file_path.replace(file_leng_name, file_leng_name_new)
file = open(file_path, 'r', encoding='utf-8')
data = file.readlines()
rowsCount = len(data)

for i in range(rowsCount):
	l = data[i]
	l_data = l.split(', ')
	columnCount = len(l_data)
	for j in range(columnCount):
		x = l_data[j]
		print(x)
