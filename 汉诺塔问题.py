def move(source,target):
    print(source,"==>",target)
def hanoi(n,source,temp,target):
    if (n==1):
        move(source,target)
    else:
        hanoi(n-1,source,target,temp) #将n-1个盘子搬到中间柱
        move(source,target)           #将最后一个盘子搬到目标柱
        hanoi(n-1,temp,source,target) #将n-1个盘子搬到目标柱
#主程序
n=int(input("输入盘子数:"))
print("移动",n,"个盘子的步骤是:")
hanoi(n,"A","B","C")
