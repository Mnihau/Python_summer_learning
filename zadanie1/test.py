def fibo(i):
    if i < 1:
        return 0
    if i == 1 or i == 2:
        return 1
    else:
        return fibo(i - 1) + fibo(i - 2)


number = int(input("choose any number: "))
print(fibo(number))
