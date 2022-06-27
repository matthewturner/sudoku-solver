from .. import Puzzle, Notary


class IterativeSolver:
    def __init__(self):
        self.change_listener = None

    def solve(self, puzzle: Puzzle):
        notary = Notary()
        notary.notarize(puzzle)
        while notary.apply_single_candidates(puzzle):
            notary.notarize(puzzle)
            if not self.change_listener is None:
                self.change_listener(puzzle)
        return len(notary.notes) == 0
