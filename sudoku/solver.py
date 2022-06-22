from . import Puzzle


class Solver:
    def solve(self, puzzle: Puzzle):
        self.__solve(puzzle, 0, 0)

    def __solve(self, puzzle: Puzzle, column: int, row: int):
        if row == puzzle.size:
            column += 1
            if column == puzzle.size:
                return True
            row = 0

        if puzzle.has_value(column, row):
            return self.__solve(puzzle, column, row + 1)

        for candidate in range(1, puzzle.size + 1):
            if puzzle.try_set(column, row, candidate):
                if self.__solve(puzzle, column, row + 1):
                    return True
                else:
                    puzzle.clear(column, row)

        return False
