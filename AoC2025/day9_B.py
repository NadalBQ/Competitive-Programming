import shapely


coordinates = []
coords = input()
while coords != "":
    a, b = map(int, coords.split(","))
    coordinates.append((a, b))
    coords = input()

polygon = shapely.Polygon(coordinates)
shapely.prepare(polygon)

maxarea = 0
for coords1 in coordinates:
    for coords2 in coordinates:
        corners = [coords1, (coords1[0], coords2[1]), coords2, (coords2[0], coords1[1])]
        area = (abs(coords1[0]-coords2[0])+1)*(abs(coords1[1]-coords2[1])+1)
        rect = shapely.Polygon(corners)
        if polygon.contains(rect) and area > maxarea:
            maxarea = area

print(maxarea)
