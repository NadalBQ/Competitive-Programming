rstr = input()
ranges = []
while rstr != "":
    r = rstr.split("-")
    ranges.append((int(r[0]), int(r[1])))
    rstr = input()

i = input()
while i != "":
    i = input()

i = -1
l = len(ranges)
while (i+1) < l:
    i += 1
    j = -1
    r1 = ranges[i]
    while (j + 1) < l:
        j += 1
        if i == (j):
            continue

        r2 = ranges[j]
        if r1[0] <= r2[0]:
            if r1[1] >= r2[0]:
                newr = (r1[0], max(r1[1], r2[1]))
                ranges[i] = newr
                ranges.pop(j)
                l -= 1
                j = -1
                i = 0
                r1 = ranges[i]

suma = 0
for r in ranges:
    print(r)
    suma += r[1] - r[0] + 1
print(suma)
