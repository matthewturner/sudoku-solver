from . import Puzzle


class Notary:
    def __init__(self):
        self.notes = {}

    def apply_single_candidates(self, puzzle: Puzzle):
        has_applied = False
        removed = []
        for location in self.notes:
            note = self.notes[location]
            if len(note) == 1:
                column, row = location
                puzzle.set(column, row, note.pop())
                removed.append(location)
                has_applied = True
        for location in removed:
            self.notes.pop(location)
        return has_applied

    def notarize(self, puzzle: Puzzle):
        for row in range(0, puzzle.size):
            for column in range(0, puzzle.size):
                if not puzzle.has_value(column, row):
                    candidates = self.notes[(column, row)] = []
                    for candidate in puzzle.candidates:
                        if puzzle.is_valid(column, row, candidate):
                            candidates.append(candidate)
        return self.notes
