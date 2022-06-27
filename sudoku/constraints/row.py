from .base import Base

class Row(Base):
    def is_valid(self, _: int, row: int, value: int):
        return not value in self.grid[row]
