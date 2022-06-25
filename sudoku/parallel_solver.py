from operator import mul

import numpy
from . import Puzzle, Solver, PuzzleSerializer
import multiprocessing


class ParallelSolver:
    def __init__(self):
        self.column_change_listener = None

    def solve(self, puzzle: Puzzle):
        solver = Solver()
        notes = solver.create_notes(puzzle)
        processes = []
        start = self.__first_empty_cell(puzzle)
        definition = PuzzleSerializer.serialize(puzzle)
        for candidate in notes[start]:
            column, row = start
            processes.append(multiprocessing.Process(
                target=self.psolve, args=(definition, column, row, candidate)))

        for proc in processes:
            proc.start()

        for proc in processes:
            proc.join()

    def __first_empty_cell(self, puzzle: Puzzle):
        for row in range(0, puzzle.size):
            for column in range(0, puzzle.size):
                if not puzzle.has_value(column, row):
                    return (column, row)
        return None

    def psolve(self, definition: str, column: int, row: int, seed: int):
        puzzle = PuzzleSerializer.deserialize(definition)
        puzzle.set(column, row, seed)

        solver = Solver()
        if solver.solve(puzzle):
            print('solution found')
