op = {"L": -1, "R": 1}
num = 50
k = 0
while True:
    
    a = input()
    o, n = a[0], int(a[1:])
    if num == 0 and op[o] == -1:
        k -= 1
    while n > 100:
        k += 1
        n -= 100
    num = (num + op[o] * n)
    if num <= 0:
        k += 1
    elif num >= 100:
        k += 1
    num = num % 100
    print(k, num)