t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    up = 0
    for v in l:
        if v == 1 or v == 3:
            up += 1
        
    print(up)
