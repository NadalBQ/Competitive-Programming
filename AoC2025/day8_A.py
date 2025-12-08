def min_distance(distances):
    min_distances = {}
    for box in distances.keys():
        mini = 1000000000
        for i in range(len(distances[box])):
            if distances[box][i] < mini:
                mini = distances[box][i]
                miniter = i
        min_distances[box] = (mini, miniter)

    mini = 1000000000
    for box in min_distances.keys():
        if min_distances[box][0] < mini:
            mini = min_distances[box][0]
            miniter = min_distances[box][1]
            minibox = box
    
    distances[minibox][miniter] = 1000000000
    distances[iter_to_box(miniter)][box_to_iter(minibox)] = 1000000000
    return (mini, minibox, miniter)


def iter_to_box(i):
    for box in distances.keys():
        if i == 0:
            return box
        i -= 1


def box_to_iter(box):
    i =0
    for b in distances.keys():
        if b == box:
            return i
        i += 1


# Implementation of Merge-Find sets
parents = {}
def find_parent(x, parents):
    rx = x
    while rx in parents:
        rx = parents[rx]
    while x != rx:
        tmp = parents[x]
        parents[x] = rx
        x = tmp
    return x, parents


def merge_boxes(x, y, parents):
    rx, parents = find_parent(x, parents)
    ry, parents = find_parent(y, parents)
    if rx != ry:
        parents[rx] = ry
    rx, parents = find_parent(rx, parents)
    ry, parents = find_parent(ry, parents)
    rx, parents = find_parent(rx, parents)
    return parents


distances = {}
box = input()
while box != "":
    box_pos = tuple(map(int, box.split(",")))
    distances[box_pos] = 0
    box = input()

for box_pos in distances.keys():
    distance = []
    for box_pos2 in distances.keys():
        if box_pos == box_pos2:
            distance.append(1000000000)
        else:
            distance.append(((box_pos[0] - box_pos2[0])**2 + (box_pos[1] - box_pos2[1])**2 + (box_pos[2] - box_pos2[2])**2)**0.5)
    distances[box_pos] = distance

counter = 0
max_count = 1000
while counter < max_count:
    dist, box, i = min_distance(distances)
    box2 = iter_to_box(i)
    x, parents = find_parent(box, parents)
    y, parents = find_parent(box2, parents)
    parents = merge_boxes(x, y, parents)
    counter += 1

p = {}
for parent in distances.keys():
    p[parent] = 1

for son, parent in parents.items():
    parent, parents = find_parent(parent, parents)
    p[parent] += 1

def get_x_biggest(p, x):
    n_biggest = []
    for _, n in p.items():
        n_biggest.sort()
        if len(n_biggest) < x:
            n_biggest.append(n)
        elif n > n_biggest[0]:
            n_biggest.append(n)
            n_biggest.pop(0)
    return n_biggest


n_biggest = get_x_biggest(p, 3)
res = 1
for n in n_biggest:
    res *= n
print(res)
