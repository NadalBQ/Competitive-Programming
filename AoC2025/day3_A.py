def get_biggest_number(s):
    s = str(s)
    biggest = 0
    big_iter = 0
    for i in range(len(s)):
        if int(s[i]) > biggest and i != len(s)-1:
            biggest = int(s[i])
            big_iter = i
    second = 0
    for j in range(big_iter+1, len(s)):
        if int(s[j]) >= second:
            second = int(s[j])
    return int(str(biggest) + str(second))


suma = 0
while True:
    n = input()
    if n == "":
        break
    suma += get_biggest_number(n)
print(suma)
    