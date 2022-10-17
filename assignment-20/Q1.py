def f1(l1):
    x = []
    for e in l1:
        if e not in x:
            x.append(e)
    return x
l1 = [eval(i) for i in input("Enter values:").split(',')]
print(f1(l1))