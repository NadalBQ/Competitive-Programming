def invalid(s):
    s = str(s)
    nums = []
    for i in range(1, len(s)//2 + 1):
        if s[0] == s[i]:
            nums.append(i)
            
    if nums == []:
        return True
    
    for n in nums:
        k = 0
        result = False
        while n+k < len(s):
            if s[0] == s[n+k] and k%n == 0:
                if len(s) < n+k+n:
                    result = True
            if s[0+k] != s[n+k]:
                result = True
            k += 1

        if result == False:
            return False

    return True
ranges = input().split(",")
suma = 0
for r in ranges:
    a, b = map(int, r.split("-"))
    for i in range(a, b + 1):
        if invalid(i) == False:
            suma += i
print(suma)