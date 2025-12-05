rstr = input()
ranges = []
while rstr != "":
    r = rstr.split("-")
    ranges.append((int(r[0]), int(r[1])))
    rstr = input()

i = input()
count = 0
while i != "":
    n = int(i)
    for r in ranges:
        if n >= r[0] and n <= r[1]:
            count += 1
            break
    i = input()
print(count)