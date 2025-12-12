presents = {}
for i in range(6):
    input()
    presents[i] = 0
    for j in range(3):
        inp = input()
        presents[i] += int(inp.count("#"))
    input()

suma = 0
areas = input()
while areas != "":
    a,indices = areas.split(":")
    indices = list(map(int, indices.strip().split()))
    area = 0
    n, m = map(int, a.split("x"))
    a = n*m
    for i in range(len(indices)):
        area += indices[i] * presents[i]
    if area <= a:
        suma += 1
    areas = input()

print(suma)
