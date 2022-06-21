from grid import Grid

class GridSerializer:
    def serialize(self):
        definition = ''
        for columns in self.values:
            for column in columns:
                if column is None:
                    definition += ' _'
                else:
                    definition += f' {column}'
            definition += '\n'
        return definition

    def deserialize(definition: str):
        scale = len(definition
                    .splitlines()[0]
                    .strip()
                    .split(' '))

        grid = Grid(scale)

        row = 0
        for line in definition.splitlines():
            column = 0
            for num in line.strip().split(' '):
                if num != '_':
                    grid.set_value(column, row, int(num))
                column += 1
            row += 1

        return grid
