n = int(input())
lista = input().split()
perms = 0
for i in range(n):
    if str(i+1) in lista:
        pass
    else:
        perms += 1
print(perms)