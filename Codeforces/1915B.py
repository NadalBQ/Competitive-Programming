nCases = int(input())
 
for i in range(nCases): # por cada caso
 
    for e in range(3): # por cada linea del caso
        line = input()
        if "?" in line:
            if "A" in line and "B" in line:
                print("C")
            if "C" in line and "B" in line:
                print("A")
            if "A" in line and "C" in line:
                print("B")