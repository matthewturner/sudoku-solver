from numpy import array


class Base:
    def __init__(self, grid: array, candidates: list):
        self.grid = grid
        self.candidates = candidates
