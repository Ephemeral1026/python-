from tkinter import *
import random
n=52
def gen_pocker(n):
    x=100
    while(x>0):
        x=x-1
        p1=random.randint(0,n-1)
        p2=random.randint(0,n-1)
        t=pocker[p1]
        pocker[p1]
        pocker[p1]=pocker[p2]
        pocker[p2]=t
    return pocker
pocker=[i for i in range(n)]
pocker=gen_pocker(n)
print(pocker)
(player1,player2,player3,player4)=([],[],[],[]) #四位牌手各自牌的图片列表
(p1,p2,p3,p4)=([],[],[],[])
root=Tk()
#创建一个Canvas，设置其背景色为白色
cv=Canvas(root,bg='white',width=700,height=600)
imgs=[]
for i in range(1,5):
    for j in range(1,14):
        imgs.insert((i-1)*13+(j-1),PhotoImage(
