cases = int(input())
for i in range(cases):
    numbuck = int(input())
    a = 0
    
    try:
        c=((input().split(" ")))
        b= (int(l) for l in c)
    except:
        b = int(input())
    a = sum(b)

    if int(a**(1/2)) * int(a**(1/2)) == a:
        print("YES")
    else:
        print("NO")