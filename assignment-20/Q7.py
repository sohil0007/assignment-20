def f1(a):
    a+=1
    def f2(b):
        c=a+b
        return c
    print(f2(4))
f1(4)        

