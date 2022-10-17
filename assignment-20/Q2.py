def prime(number):
    
    if x==1:
        print("non prime number")

    elif x==2:
        print("prime number")    
    
    else:
        for e in range(2,x):
            if x%e==0:
                print("non prime number")
                break
            else:
                print("prime number")
                break  

x = int(input("Enter a Number:"))
prime(x)                 