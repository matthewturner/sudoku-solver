from grid import Grid
from grid_serializer import GridSerializer

file = open('./samples/grid1.txt', 'r')
definition = file.read()
file.close()

grid = GridSerializer.deserialize(definition)

print()

definition = GridSerializer.serialize(grid)
print(definition)

print()
