from day_10 import part_one, invert_sublist, swap


def test_part_one():
    assert part_one('3,4,1,5', size=5) == 12


def test_invert_sublist():
    assert invert_sublist([0, 1, 2, 3, 4], 0, 3) == [2, 1, 0, 3, 4]
    assert invert_sublist([2, 1, 0, 3, 4], 3, 4) == [4, 3, 0, 1, 2]
    assert invert_sublist([4, 3, 0, 1, 2], 3, 1) == [4, 3, 0, 1, 2]
    assert invert_sublist([4, 3, 0, 1, 2], 1, 5) == [3, 4, 2, 1, 0]


def test_swap():
    assert swap([0, 1, 2, 3, 4], 0, 2) == [2, 1, 0, 3, 4]
