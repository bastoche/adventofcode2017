from day_1 import part_one, part_two, rotate, filter_equal_values, sum_as_integers


def test_part_one():
    assert part_one('1122') == 3
    assert part_one('1111') == 4
    assert part_one('1234') == 0
    assert part_one('91212129') == 9


def test_part_two():
    assert part_two('1212') == 6
    assert part_two('1221') == 0
    assert part_two('123425') == 4
    assert part_two('123123') == 12
    assert part_two('12131415') == 4


def test_rotate():
    assert rotate([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert rotate([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]


def test_filter_equal_values():
    assert filter_equal_values([1, 2, 3], [4, 5, 6]) == []
    assert filter_equal_values([1, 2, 3], [1, 2, 4]) == [1, 2]


def test_sum_as_integers():
    assert sum_as_integers(['0']) == 0
    assert sum_as_integers(['1', '2', '3']) == 6
