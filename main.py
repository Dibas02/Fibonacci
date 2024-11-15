def fib(length):
    a=0
    b=1
    print(a)
    print(b)
    for c in range(3, length+1):
        c=a+b
        a=b
        b=c
        print(c)

l = int(input("Enter the length of the fibonacci series: "))
fib(l)