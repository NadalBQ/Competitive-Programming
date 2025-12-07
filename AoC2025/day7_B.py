line = input()
indices = {}
for i in range(len(line)):
    if line[i] == "S":
        indices[i] = 1
    else:
        indices[i] = 0

line = input()
remove = []
while line != "":
    add = []
    for index in indices.keys():
        if line[index] == "^":
            if index + 1 != len(line):
                indices[index + 1] += indices[index]
            if index - 1 != -1:
                indices[index - 1] += indices[index]
            indices[index] = 0

    line = input()

counter = 0
for k, v in indices.items():
    counter += v
print(counter)