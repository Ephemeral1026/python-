import random
x = random.randrange(100,201) #产生一个[100，200]之间的随机数x
maxn = x
print(x,end="")
for i in range(2,11):
    x = random.randrange(100,201) #再产生一个[100，201]之间的随机数x
    print(x,end="")
    if x>maxn:
        maxn = x;
print("最大数:",maxn)
    
