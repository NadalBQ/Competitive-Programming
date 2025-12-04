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


last_accessible = 1
count_accessible = 0
while last_accessible:
    accessible = []
    for elem in matrix:
        neighbors = get_neighbors(elem)
        count = 0
        for neighbor in neighbors:
            if neighbor in matrix:
                count += 1
        if count < 4:
            accessible.append(elem)
    last_accessible = len(accessible)
    count_accessible += last_accessible
    for elem in accessible:
        matrix.remove(elem)
    print(last_accessible)
print(count_accessible)
