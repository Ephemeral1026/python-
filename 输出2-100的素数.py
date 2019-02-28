m=int(input("请输入一个整数"))
j=2
while j<=m-1: 
    if m%j==0: break #退出循环
    j=j+1
if (j>m-1):
    print(m,"是素数")
else:
    print(m,"不是素数")
