import sys

from numpy import array
from sudoku import *
from sudoku.solvers.dancing_links_solver import DancingLinksSolver
from sudoku.solvers.exact_cover_matrix import ExactCoverMatrix
from sudoku.solvers.link_matrix import LinkMatrix


def print_state(puzzle: Puzzle):
    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else './samples/puzzle2.txt'

    file = open(path, 'r')
    definition = file.read()
    file.close()

    puzzle = PuzzleSerializer.deserialize(definition)

    print()
    print('Puzzle:')
    print()

    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)

    print()

    solver = DancingLinksSolver()

    #solver.change_listener = print_state

    if solver.solve(puzzle):
        print()
        print('Solution found:')
        print()

        definition = PuzzleSerializer.serialize(puzzle)
        print(definition)

        print()
    else:
        print('No solution found')


def exact_cover_matrix():
    puzzle = Puzzle(grid=array([[1, 2, 3, 4],
                                [3, None, 1, 2],
                                [2, 3, None, 1],
                                [4, 1, 2, 3]]))
    matrix = ExactCoverMatrix.build_from(puzzle)
    matrix.clear_clues()

    print()
    print('Candate:  ', end='')
    for i in range(0, matrix.matrix.shape[0]):
        print(f'{(i % puzzle.size) + 1}|', end='')
    print()

    count = 0
    width = 100
    for row in matrix.matrix:
        print(f'{count}:  '.rjust(10), end='')
        for index, column in enumerate(row):
            if index >= width:
                break
            if (column):
                print('1|', end='')
            else:
                print('.|', end='')
        count += 1
        print()

    link_matrix = LinkMatrix.build_from(matrix.matrix)

    print(' Counts:', end='')
    for c in link_matrix.root.iterate_right(inclusive=True):
        print(f'{c.count}|', end='')
    print()

    for r in link_matrix.root.iterate_down(inclusive=True):
        for c in r.iterate_right(inclusive=True):
            print(f' -> ({c.column},{c.row})', end='')
        print()
    print()

    solved, solutions = link_matrix.search()
    print(solved)
    print(solutions)

    print()
    print('Candate:  ', end='')
    for i in range(0, matrix.matrix.shape[0]):
        print(f'{(i % puzzle.size) + 1}|', end='')
    print()

    count = 0
    width = 100
    for ri, row in enumerate(matrix.matrix):
        if ri in solutions:
            print(f'{ri}:  '.rjust(10), end='')
            for ci, column in enumerate(row):
                if ci >= width:
                    break
                if (column):
                    print('1|', end='')
                else:
                    print('.|', end='')
            print()

    print()
    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)
    print()

    if not solutions:
        print('booo')
        return
    for row in solutions:
        value = (row % puzzle.size) + 1
        solution_index = row // puzzle.size
        c = column_index = solution_index % puzzle.size
        r = row_index = solution_index // puzzle.size
        if value == 4:
            print(f'{row}: ({c},{r}) = {value}')
        if not puzzle.has_value(c, r):
            puzzle.set(c, r, value)

    print()
    definition = PuzzleSerializer.serialize(puzzle)
    print(definition)


if __name__ == '__main__':
    main()
    # exact_cover_matrix()
