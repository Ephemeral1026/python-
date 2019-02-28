def math(k):
    if(k==1):
        return lambda x,y:x+y
    if(k==2):
        return lambda x,y:x-y
    if(k==3):
        return lambda x,y:x*y
    if(k==4):
        return lambda x,y:x/y
#调用函数
action=math(1)
print("8+3=",action(8,3))
action=math(2)
print("8-3=",action(8,3))
action=math(3)
print("8*3=",action(8,3))
action=math(4)
print("8/3=",action(8,3))
