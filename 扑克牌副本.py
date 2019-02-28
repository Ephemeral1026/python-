import random
n=52
def getColor(x): #获取牌的花色
    color=["草花","方块","红桃","黑桃"]
    c=int(x/13)
    if c<0 or c>=4:
        return "ERROR!"
    return color[c]
def getValue(x):
    value=x % 13
    if value==0:
        return 'A'
    elif value>=1 and value<=9:
        return str(value+1)
    elif value==10:
        return 'J'
    elif value==11:
        return 'Q'
    elif value==12:
        return 'K'
def getPuk(x):
    return getColor(x)+getValue(x)
#主程序
(a,b,c,d)=([ ],[ ],[ ],[ ])       #a,b,c,d四个列表分别蹲存储4个人的牌
pocker=[i for i in range(n)]  #未洗牌之前
print(pocker)
random.shuffle(pocker)        #打乱排序
for x in range(13):           #发牌，每人13张牌
    m=x*4
    a.append(getPuk(pocker[m]))
    b.append(getPuk(pocker[m+1]))
    c.append(getPuk(pocker[m+2]))
    d.append(getPuk(pocker[m+3]))
a.sort() #牌手的牌的顺序，相当于理牌，同花色在一起
b.sort()
c.sort()
d.sort()
for x in a:
print("牌手1",end=":")
for x in b:
print(" \n牌手2",end=":")
for x in c:
print("\n牌手3",end=":")
for x in d:
print("\n牌手4",end=":")

    
