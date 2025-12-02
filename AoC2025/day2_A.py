ranges = input().split(",")
suma = 0
for r in ranges:
    a, b = map(int, r.split("-"))
    for i in range(a, b + 1):
        if str(i)[0:len(str(i))//2] == str(i)[len(str(i))//2:]:
            suma += i
print(suma)