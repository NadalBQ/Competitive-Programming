def vertical_join(numbers, index):
    result = ""
    for row in numbers:
        if row[index] == " ":
            continue
        result += row[index]
    return result


numbers = []
while True:
    line = input()
    try:
        int(line.split()[0])
        numbers.append(line)
    except:
        break
operations = line

spaces = 0
first = True
for char in operations:
    if char == "+" or char == "*":
        if not first:
            break
        first = False
    if char == " ":
        spaces += 1

suma = 0
parc_sum = 0
for i in range(len(operations)):
    if operations[i] == " ":
        pass
    else:
        suma += parc_sum
        o = operations[i]
        if o == "*":
            parc_sum = 1
        elif o == "+":
            parc_sum = 0
    num = vertical_join(numbers, i)
    if o == "*":
        if num == "":
            num = "1"
        parc_sum *= int(num)
    elif o == "+":
        if num == "":
            num = "0"
        parc_sum += int(num)
suma += parc_sum
print(suma)