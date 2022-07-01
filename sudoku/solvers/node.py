from typing_extensions import Self


class Node:
    def __init__(self, column: int, row: int, count: int = 1,
                 up: Self = None, down: Self = None,
                 left: Self = None, right: Self = None):
        self.column = column
        self.row = row
        self.count = count
        self.up = up or self
        self.down = down or self
        self.left = left or self
        self.right = right or self

    def iterate_up(self, inclusive: bool = False):
        itr = self
        if inclusive:
            yield itr
        while itr.up != self:
            itr = itr.up
            yield itr

    def iterate_down(self, inclusive: bool = False):
        itr = self
        if inclusive:
            yield itr
        while itr.down != self:
            itr = itr.down
            yield itr

    def iterate_left(self, inclusive: bool = False):
        itr = self
        if inclusive:
            yield itr
        while itr.up != self:
            itr = itr.left
            yield itr

    def iterate_right(self, inclusive: bool = False):
        itr = self
        if inclusive:
            yield itr
        while itr.right != self:
            itr = itr.left
            yield itr
