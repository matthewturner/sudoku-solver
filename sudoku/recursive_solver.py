from . import Puzzle, Notary


class RecursiveSolver:
    def __init__(self):
        self.column_change_listener = None

    def solve(self, puzzle: Puzzle):
        notary = Notary()
        notary.notarize(puzzle)
        notary.apply_single_candidates(puzzle)
        return self.__solve(puzzle, notary, 0, 0)

    def __solve(self, puzzle: Puzzle, notary: Notary, column: int, row: int):
        if row == puzzle.size:
            column += 1
            if column == puzzle.size:
                return True
            row = 0
            if not self.column_change_listener is None:
                self.column_change_listener((column, row), puzzle)

        if puzzle.has_value(column, row):
            return self.__solve(puzzle, notary, column, row + 1)

        for candidate in notary.notes[(column, row)]:
            if puzzle.try_set(column, row, candidate):
                if self.__solve(puzzle, notary, column, row + 1):
                    return True
                else:
                    puzzle.clear(column, row)

        return False
