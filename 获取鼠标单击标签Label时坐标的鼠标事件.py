from tkinter import *
def leftClick(event): #定义的函数监听鼠标事件
    print("x轴坐标:",event.x)
    print("y轴坐标:",event.y)
    print("相对于屏幕左上角x轴坐标:",event.x_root)
    print("相对于屏幕左上角y轴坐标:",event.y_root)
root=Tk()
lab=Label(root,text="hello") #实例化一个Label
lab.pack() #显示Label组件
#给Label绑定鼠标监听事件
lab.bind("<Button-1>",leftClick)
root.mainloop()
