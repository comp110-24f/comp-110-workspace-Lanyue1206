"""Practice of importing functions from different files."""

__author__ = "730679606"


def get_coords(xs: str, ys: str) -> None:
    index1 = 0
    index2 = 0
    while index1 < len(xs):
        while index2 < len(ys):
            print((int(xs[index1]), int(ys[index2])))
            index2 += 1
        index1 += 1
        index2 = 0
