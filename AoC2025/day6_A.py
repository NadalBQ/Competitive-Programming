numbers = []
while True:
    line = input().split()
    try:
        int(line[0])
        n = list(map(int, line))
        numbers.append(n)
    except:
        break
operations = line

suma = 0
parc_sum = 0
for i in range(len(operations)):
    o = operations[i]
    suma += parc_sum
    if o == "*":
        parc_sum = 1
    elif o == "+":
        parc_sum = 0
    for j in range(len(numbers)):
        if o == "*":
            parc_sum *= numbers[j][i]
        elif o == "+":
            parc_sum += numbers[j][i]
suma += parc_sum
print(suma)