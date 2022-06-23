from . import Puzzle


class Solver:
    def __init__(self):
        self.row_change_listener = None

    def solve(self, puzzle: Puzzle):
        return self.__solve(puzzle, 0, 0)

    def __solve(self, puzzle: Puzzle, column: int, row: int):
        if row == puzzle.size:
            if not self.row_change_listener is None:
                self.row_change_listener(puzzle)

            column += 1
            if column == puzzle.size:
                return True
            row = 0

        if puzzle.has_value(column, row):
            return self.__solve(puzzle, column, row + 1)

        for candidate in puzzle.candidates:
            if puzzle.try_set(column, row, candidate):
                if self.__solve(puzzle, column, row + 1):
                    return True
                else:
                    puzzle.clear(column, row)

        return False
