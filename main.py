import sys
from sudoku import *
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

    solver = IterativeSolver()

    solver.change_listener = print_state

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
    puzzle = Puzzle(grid=[[1, 2, 3, 4],
                          [3, None, 1, 2],
                          [2, 3, None, 1],
                          [4, 1, 2, 3]])
    matrix = ExactCoverMatrix.build_from(puzzle)
    matrix.clear_clues()
    count = 0
    width = 100
    for row in matrix.matrix:
        print(f'{count}:  '.rjust(6), end='')
        for index, column in enumerate(row):
            if index >= width:
                break
            if (column):
                print('1', end='')
            else:
                print('.', end='')
        count += 1
        print()
    print()
    print()

    link_matrix = LinkMatrix.build_from(matrix.matrix)
    for r in link_matrix.root.iterate_down(inclusive=True):
        for c in r.iterate_right(inclusive=True):
            print(f' -> ({c.column},{c.row})', end='')
        print()
    print()

    x, y = link_matrix.search()
    print(x)
    print(y)


if __name__ == '__main__':
    # main()
    exact_cover_matrix()
