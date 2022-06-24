from . import Puzzle


class PuzzleSerializer:
    def serialize(puzzle: Puzzle):
        justification = 2
        only_numbers = 10 in puzzle.candidates
        if only_numbers:
            justification = len(str(puzzle.size)) + 1

        definition = ''

        for row in puzzle.grid:
            for value in row:
                if value is None:
                    definition += '_'.rjust(justification)
                else:
                    if only_numbers:
                        definition += str(value).rjust(justification)
                    else:
                        if value <= 9:
                            definition += str(value).rjust(justification)
                        else:
                            definition += chr(value).rjust(justification)
            definition += '\n'
        return definition

    def deserialize(definition: str):
        while '  ' in definition:
            definition = definition.replace('  ', ' ')

        grid = []

        contains_letters = False
        contains_numbers = False
        for line in definition.splitlines():
            row = []
            grid.append(row)
            for num in line.strip().split(' '):
                if num == '_':
                    row.append(None)
                else:
                    number = PuzzleSerializer.to_number(num)
                    if number <= 9:
                        contains_numbers = True
                    if number >= ord('A'):
                        contains_letters = True
                    row.append(number)

        candidates = None
        if contains_letters and contains_numbers:
            candidates = list(range(0, 10)) + list(range(ord('A'), ord('G')))
        elif contains_letters:
            candidates = range(ord('A'), ord('Z'))
        else:
            candidates = range(1, len(grid) + 1)

        return Puzzle(grid=grid, candidates=candidates)

    def to_number(candidate: str):
        if len(candidate) == 1:
            if ord(candidate) in range(ord('A'), ord('Z')):
                return ord(candidate)
        return int(candidate)
