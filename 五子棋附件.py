from tkinter import *
from tkinter.messagebox import *
root=Tk()

turn=0
map=[[""for y in range(15)]for x in range(15)]
root.title("五子棋-陈临歆")
back=[] #用于悔棋，保存下过棋子的图形对象id及位置坐标
cv=Canvas(root,bg='green',width=610,height=610)

cv.bind("<Button-1>",callback)#绑定鼠标左键事件，下棋功能
cv.bind("<Button-3>",huiqi)    #绑定鼠标右键事件，悔棋功能
cv.pack()
root.mainloop()
