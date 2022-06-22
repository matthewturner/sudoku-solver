from . import Puzzle


class PuzzleSerializer:
    def serialize(puzzle):
        definition = ''
        for row in puzzle.grid:
            for column in row:
                if column is None:
                    definition += ' _'
                else:
                    definition += f' {column}'
            definition += '\n'
        return definition

    def deserialize(definition: str):
        size = len(definition
                   .splitlines()[0]
                   .strip()
                   .split(' '))

        puzzle = Puzzle(size)

        row = 0
        for line in definition.splitlines():
            column = 0
            for num in line.strip().split(' '):
                if num != '_':
                    puzzle.set_value(column, row, int(num))
                column += 1
            row += 1

        return puzzle
