def f1(str_1):
    
    l1=[]
    for e in str_1:
        if e.isupper():
            l1.append(e)

    l2=[]
    for i in str_1:
        if i.islower():
            l2.append(i)

    print("{} letters is upper case & {} letters is lower case".format(len(l1),len(l2)))

str_1 = "ABCDefghi"
f1(str_1)                    
