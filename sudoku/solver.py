from . import Puzzle


class Solver:
    def solve(self, puzzle: Puzzle):
        for row in range(0, puzzle.size):
            for column in range(0, puzzle.size):
                if puzzle.value(column, row) is None:
                    for candidate in range(1, puzzle.size + 1):
                        if puzzle.is_valid(column, row, candidate):
                            puzzle.set_value(column, row, candidate)
