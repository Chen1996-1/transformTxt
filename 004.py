from tkinter import *
from tkinter.ttk import Treeview

#排序函数

#点击复制到粘贴板

window=Tk()
window.geometry('500x450')
cols = ("姓名", "IP地址")
ybar=Scrollbar(window,orient='vertical')      #竖直滚动条 
tree=Treeview(window,show='headings',columns=cols,yscrollcommand=ybar.set)
ybar['command']=tree.yview      
#表头设置
for col in cols:
  tree.heading(col,text=col)             #行标题
  tree.column(col,width=80,anchor='w')   #每一行的宽度,'w'意思为靠右
#插入数据
for i in range(1,500):
  tree.insert("","end",values=("john","1.1.1.1"+str(i)))

tree.grid(row=0,column=0)				#grid方案
ybar.grid(row=0,column=1,sticky='ns')   
#ybar.pack(side='right',fill='y')		#pack方案
#tree.pack(fill='x')
window.mainloop()
