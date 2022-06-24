from . import Puzzle


class Solver:
    def __init__(self):
        self.column_change_listener = None

    def solve(self, puzzle: Puzzle):
        notes = self.__create_notes(puzzle)
        self.__apply_single_candidates(puzzle, notes)
        return self.__solve(puzzle, notes, 0, 0)

    def __solve(self, puzzle: Puzzle, notes: dict, column: int, row: int):
        if row == puzzle.size:
            column += 1
            if column == puzzle.size:
                return True
            row = 0
            if not self.column_change_listener is None:
                self.column_change_listener((column, row), puzzle)

        if puzzle.has_value(column, row):
            return self.__solve(puzzle, notes, column, row + 1)

        for candidate in notes[(column, row)]:
            if puzzle.try_set(column, row, candidate):
                if self.__solve(puzzle, notes, column, row + 1):
                    return True
                else:
                    puzzle.clear(column, row)

        return False

    def __apply_single_candidates(self, puzzle: Puzzle, notes: dict):
        for location in notes:
            note = notes[location]
            if len(note) == 1:
                column, row = location
                puzzle.set(column, row, note[0])
                note.clear()

    def __create_notes(self, puzzle: Puzzle):
        notes = {}
        for row in range(0, puzzle.size):
            for column in range(0, puzzle.size):
                if not puzzle.has_value(column, row):
                    candidates = notes[(column, row)] = []
                    for candidate in puzzle.candidates:
                        if puzzle.is_valid(column, row, candidate):
                            candidates.append(candidate)
        return notes
