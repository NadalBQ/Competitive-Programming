cases = int(input())
for i in range(cases):
    a = int(input())
    line = input()
    suma = 0
    for char in line:
        if char == "+":
            suma += 1
        elif char == "-":
            suma -= 1
        else:
            break
    if suma < 0:
        print(suma * (-1))
    else:
        print(suma)