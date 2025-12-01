op = {"L": -1, "R": 1}
num = 50
k = 0
while True:
    a = input()
    o, n = a[0], int(a[1:])
    num = (num + op[o] * n) % 100
    if num == 0:
        k += 1
    print(k)