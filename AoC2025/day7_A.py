line = input()
indices = []
for i in range(len(line)):
    if line[i] == "S":
        indices.append(i)
        break

counter = 0
line = input()
while line != "":
    add = []
    remove = []
    for index in indices:
        if line[index] == "^":
            remove.append(index)
            counter += 1
            if index + 1 != len(line):
                add.append(index + 1)
            if index - 1 != -1:
                add.append(index - 1)
    for i in remove:
        if i in indices:
            indices.remove(i)
    for i in add:
        if line[i] != "^" and not i in indices:
            indices.append(i)
    indices.sort()
    line = input()
print(counter)