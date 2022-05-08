def Primenums(num):
    count = 0
    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i, end=",")
            count += 1
    print("\ntotal number of prime nums present in the given number=(",num,") are" ,count)
        
        
a = Primenums(100)

