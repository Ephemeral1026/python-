def f(x):
    if x==2:
        return 1
    else:
        return(f(x-1)+x*x)
print(f(5))
