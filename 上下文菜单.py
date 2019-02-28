from tkinter import *
def popup(event): #右键事件处理函数
    menubar.post( event.x_root,event.y_root) #在鼠标右键位置显示菜单
def hello1():
    print("我是剪切命令")
def hello2():
    print("我是复制命令")
def hello3():
    print("我是粘贴命令")
root=Tk()
root.geometry("300x150")
menubar=Menu(root)
menubar.add_command(label='剪切',command=hello1)
menubar.add_command(label='复制',command=hello2)
menubar.add_command(label='粘贴',command=hello3)
#创建Entry组件界面
s=StringVar()
s.set("大家好，这是测试上下文菜单")
entryCd=Entry(root,textvariable=s)
entryCd.pack()
root.bind('<Button-3>',popup)
root.mainloop()

    
