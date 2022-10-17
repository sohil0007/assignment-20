def even(l1):
    x = []
    for e in l1:
        if e%2==0:
            x.append(e)
    return x

print(even([1,2,3,4,5,6,7,8,9]))    