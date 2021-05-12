import numpy as np
import tkinter
from tkinter import *



file_path = '111.txt'

file_arry = np.loadtxt(file_path, encoding='utf-8', dtype=str, delimiter=', ')
text_arry = str(file_arry)

import tkinter as tk
 
root = tk.Tk()
 
text = tk.Text(root)
text.pack()
 
# "insert" 索引表示插入光标当前的位置
text.insert("insert", text_arry)

 
root.mainloop()