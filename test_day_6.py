from day_6 import part_one, redistribute


def test_part_one():
    assert part_one('0 2 7 0') == 5


def test_redistribute():
    assert redistribute([0, 2, 7, 0]) == [2, 4, 1, 2]
