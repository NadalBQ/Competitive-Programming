cases = int(input())
 
for i in range(cases):
    case = input().split()
    if case[0] == case[1]:
        print(int(case[2]))
    if case[0] == case[2]:
        print(int(case[1]))
    if case[2] == case[1]:
        print(int(case[0]))