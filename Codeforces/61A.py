a = input()
b = input()
n = len(a)
a, b = (int(e, 2) for e in (a, b))
res = bin(a ^ b)[2:]
k = len(res)
while k != n:
    k += 1
    res = "0" + res
print(res)