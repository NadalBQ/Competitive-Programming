def get_biggest_number(s, it=0):
    s = str(s)
    s = [int(x) for x in s]
    biggest = 0
    big_iter = 0
    for i in range(len(s) - 12 + it):
        if int(s[i]) > biggest:
            biggest = int(s[i])
            big_iter = i
    s = s[big_iter+1:]
    string = ""
    for i in range(len(s)):
        string += str(s[i])
    return biggest, string


def build_string(s):
    it = 0
    res = ""
    while True:
        it += 1
        num, s = get_biggest_number(s, it)
        res += str(num)
        if ((len(res) + len(s)) == 12):
            res += s
        if len(res) == 12:
            return res
    

suma = 0
while True:
    n = input()
    if n == "":
        break
    suma += int(build_string(n))
print(suma)
    