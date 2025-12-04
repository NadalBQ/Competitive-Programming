def get_neighbors(pos):
    neighbors = []
    i, j = pos
    i -= 1
    j -= 1
    for x in range(3):
        for y in range(3):
            if (i, j) != pos:
                neighbors.append((i, j))
            j += 1
        i += 1
        j -= 3
    return neighbors


line = input()
l = len(line)
matrix = []
j = -1
while line != "":
    j += 1
    for i in range(len(line)):
        if line[i] == "@":
            matrix.append((j, i))
    line = input()


accessible = []
for elem in matrix:
    neighbors = get_neighbors(elem)
    count = 0
    for neighbor in neighbors:
        if neighbor in matrix:
            count += 1
    if count < 4:
        accessible.append(elem)
print(len(accessible))
