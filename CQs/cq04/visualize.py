"""Practice of importing functions from different files."""

__author__ = "730679606"


from CQs.cq04.concatenation import concat

x = "123"
y = "abc"
print(concat(x, y))

from CQs.cq04.coordinates import get_coords

print(get_coords(x, y))
