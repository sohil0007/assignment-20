def f1():
    print("enter 3 numbers")
    i=1
    l1=[]
    while i<=3:
        a = int(input())
        l1.append(a)
        i+=1

    print("min of three numbers is",min(l1))
    
f1()