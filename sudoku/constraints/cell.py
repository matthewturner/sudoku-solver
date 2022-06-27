from .base import Base


class Cell(Base):
    def is_valid(self, _: int, __: int, value: int):
        return value in self.candidates
