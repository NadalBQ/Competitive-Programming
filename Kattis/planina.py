a = int(input())
res = 9
for i in range(a-1):
    res = (res**(1/2) + res**(1/2)-1)**2
print(int(res))