n = int(input())
l = set(range(1, n+1))
l1 = list(map(int, input().split()[1:]))
l2 = list(map(int, input().split()[1:]))

s = set(l1 + l2)
if s == l:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')