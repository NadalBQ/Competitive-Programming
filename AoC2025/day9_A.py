

coordinates = []
coords = input()
while coords != "":
    a, b = map(int, coords.split(","))
    coordinates.append((a, b))
    coords = input()

maxarea = 0
for i in range(len(coordinates)):
    a, b = coordinates[i]
    for j in range(i+1, len(coordinates)):
        c, d = coordinates[j]
        area = (abs(a-c) + 1) * (abs(d-b) + 1)
        if area > maxarea:
            maxarea = area

print(maxarea)