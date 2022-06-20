from argparse import ArgumentError
from math import sqrt


class Grid:
    def __init__(self, scale: int):
        if sqrt(scale).is_integer() is False:
            raise ArgumentError(None, f'{scale} is not a square')
