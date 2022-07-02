from typing_extensions import Self
from numpy import array
from pyparsing import col
from sudoku.solvers.node import Node


class LinkMatrix:
    def __init__(self):
        self.root: Node = None
        self.rows: list[Node] = None
        self.columns: list[Node] = None

    def insert_node(self, column: int, row: int) -> None:
        node: Node = Node(column, row)
        self.__insert_in_row(column, row, node)
        self.__insert_in_column(column, row, node)
        self.get_column_header_for(node).count += 1

    def __insert_in_column(self, column: int, row: int, node: Node):
        for n in self.columns[column].iterate_down(inclusive=True):
            if n.down.row == -1 or n.down.row > row:
                break
        node.down = n.down
        node.up = n
        node.down.up = node
        n.down = node

    def __insert_in_row(self, column: int, row: int, node: Node):
        n = self.root
        for n in self.rows[row].iterate_right(inclusive=True):
            if n.right.column == -1 or n.right.column > column:
                break
        if n.column == column:
            return

        node.right = n.right
        node.left = n
        node.right.left = node
        n.right = node

    def cover(self, node: Node) -> None:
        column_header = self.get_column_header_for(node)
        column_header.right.left = column_header.left
        column_header.left.right = column_header.right
        for column_node in column_header.iterate_down():
            for row_node in column_node.iterate_right():
                row_node.up.down = row_node.down
                row_node.down.up = row_node.up
                self.get_column_header_for(row_node).count -= 1

    def uncover(self, node: Node) -> None:
        column_header = self.get_column_header_for(node)
        for column_node in column_header.iterate_up():
            for row_node in column_node.iterate_left():
                row_node.up.down = row_node
                row_node.down.up = row_node
                self.get_column_header_for(row_node).count += 1
        column_header.right.left = column_header
        column_header.left.right = column_header

    def get_column_header_for(self, node: Node) -> Node:
        if node.column == -1:
            return self.root
        return self.columns[node.column]

    @staticmethod
    def build_from(matrix: array) -> Self:

        lm = LinkMatrix()

        lm.__initialize(matrix.shape)
        lm.__initialize_root_node()
        lm.__initialize_row_headers()
        lm.__initialize_column_headers()
        lm.__hook_root_node()
        lm.__populate_from(matrix)

        return lm

    def __populate_from(self, matrix: array):
        column_count, row_count = matrix.shape
        for column in range(column_count):
            for row in range(row_count):
                if matrix[row, column]:
                    self.insert_node(column, row)

    def __initialize_root_node(self):
        self.root = Node(-1, -1)

    def __hook_root_node(self):
        self.root.right = self.columns[0]
        self.root.left = self.columns[-1]
        self.root.down = self.rows[0]
        self.root.up = self.rows[-1]

    def __initialize(self, shape: tuple[int, int]):
        column_count, row_count = shape
        self.rows = [Node(row=i, column=-1)
                     for i in range(row_count)]
        self.columns = [
            Node(row=-1, column=i) for i in range(column_count)]

    def __initialize_column_headers(self):
        for i, node in enumerate(self.columns):
            node.up = node
            node.down = node
            if i < len(self.columns) - 1:
                node.right = self.columns[i + 1]
            else:
                node.right = self.root
            if i > 0:
                node.left = self.columns[i - 1]
            else:
                node.left = self.root

    def __initialize_row_headers(self):
        for i, node in enumerate(self.rows):
            node.right = node
            node.left = node

            if i < len(self.rows) - 1:
                node.down = self.rows[i + 1]
            else:
                node.down = self.root
            if i > 0:
                node.up = self.rows[i - 1]
            else:
                node.up = self.root
