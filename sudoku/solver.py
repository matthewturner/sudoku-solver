from . import Puzzle


class Solver:
    def solve(self, puzzle: Puzzle):
        self.__solve_cell(puzzle, 0, 0)

    def __solve_cell(self, puzzle: Puzzle, column: int, row: int):
        if row == puzzle.size:
            column += 1
            row = 0

        if column == puzzle.size:
            return True

        if puzzle.value(column, row) is not None:
            return self.__solve_cell(puzzle, column, row + 1)

        for candidate in range(1, puzzle.size + 1):
            if puzzle.try_set(column, row, candidate):
                if self.__solve_cell(puzzle, column, row + 1):
                    return True
                else:
                    puzzle.clear(column, row)

        return False
