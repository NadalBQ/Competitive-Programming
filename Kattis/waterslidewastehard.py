import sys
input = sys.stdin.readline

def l1(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

n = int(input())

class tobogan():
    def __init__(self, x, y, x2, y2, w):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.w = w

    def litres(self): 
        return self.w
    
    def start(self): 
        return (self.x,self.y)

    def end(self): 
        return (self.x2,self.y2)

suma = 0
inicios = set()
finales = []
toboganes = []

for i in range(n):
    a = tobogan(*map(int, input().split()))
    toboganes.append(a)
    inicios.add(a.start())
    suma += a.litres()

toboganes_by_start = {}
for t in toboganes:
    toboganes_by_start[t.start()] = t

finales.append((0,0))

best_dist = {}
for inicio in inicios:
    best_dist[inicio] = l1((0,0), inicio)

while inicios:
    lmax = 10000000
    min_inicio = None

    for inicio in inicios:
        if best_dist[inicio] < lmax:
            lmax = best_dist[inicio]
            min_inicio = inicio

    suma += lmax

    nuevo_final_1 = min_inicio
    nuevo_final_2 = toboganes_by_start[min_inicio].end()

    inicios.remove(min_inicio)
    del best_dist[min_inicio]

    for inicio in inicios:
        d1 = l1(nuevo_final_1, inicio)
        if d1 < best_dist[inicio]:
            best_dist[inicio] = d1

        d2 = l1(nuevo_final_2, inicio)
        if d2 < best_dist[inicio]:
            best_dist[inicio] = d2

print(suma)
