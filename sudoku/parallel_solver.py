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
        solver.apply_single_candidates(puzzle, notes)
        processes = []
        start = self.__first_empty_cell(puzzle)
        definition = PuzzleSerializer.serialize(puzzle)
        manager = multiprocessing.Manager()
        results = []
        for candidate in notes[start]:
            column, row = start
            result = manager.dict()
            results.append(result)
            processes.append(multiprocessing.Process(
                target=self.psolve, args=(result, definition, column, row, candidate)))

        for index, proc in enumerate(processes):
            proc.start()
            results[index]['pid'] = proc.pid

        for proc in processes:
            proc.join()

        for result in results:
            if result['success']:
                solution = PuzzleSerializer.deserialize(result['grid'])
                puzzle.update_from(solution)
                return True

        return False

    def __first_empty_cell(self, puzzle: Puzzle):
        for row in range(0, puzzle.size):
            for column in range(0, puzzle.size):
                if not puzzle.has_value(column, row):
                    return (column, row)
        return None

    def psolve(self, result: dict, definition: str, column: int, row: int, seed: int):
        pid = result['pid']
        print(f'Solving ({column},{row}) with {seed} ({pid})...')

        puzzle = PuzzleSerializer.deserialize(definition)
        puzzle.set(column, row, seed)

        solver = Solver()
        if solver.solve(puzzle):
            result['success'] = True
            result['grid'] = PuzzleSerializer.serialize(puzzle)
        else:
            result['success'] = False
