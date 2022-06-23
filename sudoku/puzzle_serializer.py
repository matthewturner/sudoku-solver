from . import Puzzle


class PuzzleSerializer:
    def serialize(puzzle: Puzzle):
        justification = len(str(puzzle.size)) + 1
        definition = ''
        for row in puzzle.grid:
            for value in row:
                if value is None:
                    definition += '_'.rjust(justification)
                else:
                    definition += str(value).rjust(justification)
            definition += '\n'
        return definition

    def deserialize(definition: str):
        while '  ' in definition:
            definition = definition.replace('  ', ' ')

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
                    puzzle.set(
                        column, row, PuzzleSerializer.to_number(num))
                column += 1
            row += 1

        return puzzle

    def to_number(candidate: str):
        if len(candidate) == 1:
            if ord(candidate) in range(ord('A'), ord('Z')):
                return ord(candidate) - ord('@')
        return int(candidate)
