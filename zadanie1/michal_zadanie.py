number = int(input("choose any number: "))
fibo = ()
a = 0
b = 1
c = a + b
if number == 1 or number == 2:
    fibo = 1
elif number == 0:
    fibo = 0
else:
    for number in range(2, number):
        a = b
        b = c
        c = a + b
        fibo = c
print(fibo)
