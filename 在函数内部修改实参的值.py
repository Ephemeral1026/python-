def modify1(m,k):
     m=2
     k=[4,5,6]
     return
def modify2(m,k):
    m=2
    k[0]=0 #同时修改了实参的内容
    return
#主程序
n=100
L=[1,2,3]
modify1(n,L)
print(n)
print(L)
modify2(n,L)
print(n)
print(L)
