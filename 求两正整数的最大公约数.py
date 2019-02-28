num1=int(input("请输入第一个数字:"))
num2=int(input("请输入第二个数字:"))
m=num1
n=num2
if m<n:
    t=m
    m=n
    n=t
r=m % n;
while r!=0:
    m=n
    n=r
    r=m%n
print(num1,"和",num2,"的最大公约数为",n)
