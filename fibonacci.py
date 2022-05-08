def fib(num):
    a, b = 0, 1
    count = 0
    if num == 0:
        print("wrong")
    elif num == 1:
        print(num)
    else:
        while count <= num:
            print(a)
            c = a + b
            a = b
            b = c
            count += 1

num = int(input())
fib(num)

