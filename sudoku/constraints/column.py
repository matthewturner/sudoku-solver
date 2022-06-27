from .base import Base

class Column(Base):
    def is_valid(self, column: int, _: int, value: int):
        for row in self.grid:
            if row[column] == value:
                return False
        return True
