import sys

from numpy import array
from sudoku import *
from sudoku.solvers.dancing_links_solver import DancingLinksSolver
from sudoku.solvers.exact_cover_matrix import ExactCoverMatrix


def print_state(puzzle: Puzzle):
    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)


def print_matrix(puzzle: Puzzle, ecm: ExactCoverMatrix, covering_rows: list[int] = None):
    row_count, column_count = ecm.matrix.shape

    if puzzle.size >= 16:
        print('Exact cover matrix too big to display')
        print(f'\tColumns >: {column_count}')
        print(f'\tRows    v: {row_count}')
        print()
        return

    print('Candidate:  '.rjust(18), end='')
    max_width = 66
    for i in range(0, column_count):
        if i >= max_width:
            break
        candidate = PuzzleSerializer.serialize_value(
            puzzle.candidates[(i % puzzle.size)])
        print(f'{candidate}|', end='')
    print()

    if covering_rows is None:
        for ri, row in enumerate(ecm.matrix):
            if True not in row:
                continue
            print_row(ecm, ri, row, max_width)
        print()
        print('Exact cover matrix')
        print(f'\tColumns >: {column_count}')
        print(f'\tRows v:    {row_count}')
        print()
    else:
        covering_rows.sort()
        for ri in covering_rows:
            row = ecm.matrix[ri]
            print_row(ecm, ri, row, max_width)
        print()


def print_row(ecm: ExactCoverMatrix, ri: int, row, max_width: int):
    _, sc, sr, sv = ecm.translate([ri])[0]
    print(f'({sc},{sr})->{sv}', end='')
    print(f'{ri}:  '.rjust(10), end='')
    for ci, column in enumerate(row):
        if ci >= max_width:
            break
        if (column):
            print('x|', end='')
        else:
            print('.|', end='')
    print()


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './samples/puzzle2.txt'

    file = open(path, 'r')
    definition = file.read()
    file.close()

    original_puzzle = PuzzleSerializer.deserialize(definition)
    puzzle = PuzzleSerializer.deserialize(definition)

    print()
    print('Puzzle:')
    print()
    print_state(puzzle)
    print()

    solver = DancingLinksSolver()

    solver.on_matrix_built_listener = print_matrix
    solver.on_clues_filtered_listener = print_matrix
    solver.on_covered_listener = print_matrix
    solver.on_solution_found = print_matrix

    if solver.solve(puzzle):
        print()
        print('Solution found:')
        print()

        print_state(original_puzzle)
        print_state(puzzle)

        print()
    else:
        print('No solution found')
        print()


if __name__ == '__main__':
    main()
