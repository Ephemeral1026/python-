def win_lose(): #输赢判断
    #扫描整个棋盘,判断是否连成五颗
    a=str(turn)
    print("a=",a)
    for i in range(0,11):
        #判断X=Y轴上是否形成五子连珠
        for j in range(0,11):
            if map[i][j]==a and map[i+1][j+1]==a and map[i+2][j+2]==a and map[i+3][j+3]==a and map[i+4][j+4]==a:
                print("X=Y轴上形成五子连珠")
                return True
    for i in range(4,15):
        #判断X=-Y轴上是否形成五子连珠
        for j in range(0,11):
            if map[i][j]==a and map[i-1][j+1]==a and map[i-2][j+2]==a and map[i-3][j+3]==a and map[i-4][j+4]==a:
                print("X=-Y轴上形成五子连珠")
                return True

    for i in range(0,15):
        #判断Y轴上是否形成五子连珠
        for j in range(4,15):
             if map[i][j]==a and map[i][j-1]==a and map[i][j-2]==a and map[i][j-3]==a and map[i][j-4]==a:
                 print("Y轴上形成五子连珠")
                 return True

    for i in range(0,11):
        #判断X轴上是否形成五子连珠
        for j in range(0,15):
            if map[i][j]==a and map[i+1][j]==a and map[i+2][j]==a and map[i+3][j]==a and map[i+4][j]==a:
                print("X轴上形成五子连珠")
                return True
    return False

def checkWin(x,y):
    flag=False
    count=1 #保存共有相同颜色多少棋子相逢
    color=map[x][y]
    #通过循环来做棋子相连的判断
    #横向的判断
    #判断横向是否有5个棋子相连，特点是纵坐标相同，即map[x][y]中的y值是相同的
    i=1
    while color==map[x+i][y]: #向右统计
        count=count+1
        i=i+1
    i=1
    while color==map[x-i][y]: #向左统计
        count=count+1
        i=i+1
    if count>=5:
        flag=True

    #纵向判断
    i2=1
    count2=1
    while color==map[x][y+i2]:
        count2=count2+1
        i2=i2+1
    i2=1
    while color==map[x][y-i2]:
        count2=count2+1
        i2=i2+1
    if count2>=5:
        flag=True

    #斜方向的判断(右上+左下)
    i3=1
    count3=1
    while color==map[x+i3][y-i3]:
        count3=count3+1
        i3=i3+1
    i3=1
    while color==map[x-i3][y+i3]:
        count3=count3+1
        i3=i3+1
    if count3>=5:
        flag=True

    #斜方向的判断(右下+左上)
    i4=1
    count4=1
    while color==map[x+i4][y+i4]:
        count4=count4+1
        i4=i4+1
    i4=1
    while color==map[x-i4][y+i4]:
        count4=count4+1
        i4=i4+1
    if count4>=5:
        flag=True
    return flag

#输出走棋信息
def print_map():
    for i in range(0,15):
        for j in range(0,15):
            print(map[i][j],end='')
        print('w')


#走棋函数
def callback(event):
    global turn
    #print("clicked at",event.x,event.y,turn)
    x=(event.x)//40
    y=(event.y)//40
    print("clicked at",x,y,turn)
    if map[x][y]!="":
        showinfo(title="提示",message="已有棋子")
    else:
        img1=imgs[turn]
        id=cv.create_image((x*40+20,y*40+20),image=img1) 
        back.append((id,x,y))
        cv.pack()        
        map[x][y]=str(turn)
        print_map() #输出map地图
        if checkWin(x,y):
            if turn==0:
                showinfo(title="提示",message="黑方你赢了")
            else:
                showinfo(title="提示",message="白方你赢了")
        #换下一方走棋
        if turn==0:
            turn=1
        else:
            turn=0

#悔棋函数
def huiqi(event):
    global turn
    if len(back)==0:
        showinfo(title="提示",message="已经没有任何棋子了!!!")
        return
    m=back.pop()
    id=m[0]
    x=m[1]
    y=m[2]
    map[x][y]=''
    cv.delete(id)
    #换上一方走棋
    if turn==0:
        turn=1
    else:
        turn=0
    
        
                
#画棋盘
def drawQiPan(): #画棋盘
    for i in range(0,15):
        cv.create_line(20,20+40*i,580,20+40*i,width=2)
    for i in range(0,15):
        cv.create_line(20+40*i,20,20+40*i,580,width=2)
    cv.pack()



from tkinter import *
from tkinter.messagebox import *
root=Tk()
imgs=[PhotoImage(file='G:\\BlackStone.gif'),PhotoImage(file='G:\\WhiteStone.gif')]
turn=0
map=[[""for y in range(15)]for x in range(15)]
root.title("五子棋-陈临歆")
back=[] #用于悔棋，保存下过棋子的图形对象id及位置坐标
cv=Canvas(root,bg='green',width=610,height=610)
drawQiPan()

cv.bind("<Button-1>",callback)#绑定鼠标左键事件，下棋功能
cv.bind("<Button-3>",huiqi)    #绑定鼠标右键事件，悔棋功能
cv.pack()
root.mainloop()        
        
    
        
            
                
            
            
        
            
                
            
