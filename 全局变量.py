x=2
def fun1():
    print(x,end=" ")
def fun2():
    global x
    x=x+1
    print(x,end=" ")
fun1()
fun2()
print(x,end=" ")
    
