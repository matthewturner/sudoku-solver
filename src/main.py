from grid import Grid

file = open('./samples/grid1.txt', 'r')
definition = file.read()
file.close()

grid = Grid.parse(definition)

print()

grid.print()

print()
