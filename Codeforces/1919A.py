cases = int(input())
for i in range(cases):
    a, b = map(int, input().split())
    if a % 2 == 0 and b % 2 == 0:
        print("Bob")
    elif a % 2 != 0 and b % 2 != 0:
        print("Bob")
    else:
        print("Alice")