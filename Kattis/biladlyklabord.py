a = input()
last = ""
printer = ""
for l in a:
    if l == last:
        continue
    last = l
    printer += l
print(printer)