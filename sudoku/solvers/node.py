from typing_extensions import Self


class Node:
    def __init__(self, column: int, row: int,
                 up: Self, down: Self, left: Self, right: Self):
        self.column = column
        self.row = row
        self.up = up or self
        self.down = down or self
        self.left = left or self
        self.right = right or self

    def iterate_up(self):
        itr = self
        while itr.up != self:
            itr = itr.up
            yield itr

    def iterate_down(self):
        itr = self
        while itr.down != self:
            itr = itr.down
            yield itr

    def iterate_left(self):
        itr = self
        while itr.up != self:
            itr = itr.left
            yield itr

    def iterate_right(self):
        itr = self
        while itr.right != self:
            itr = itr.left
            yield itr
