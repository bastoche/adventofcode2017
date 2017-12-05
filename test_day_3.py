from day_3 import part_one, get_closest_point, get_cardinal_directions, get_odd_square_below, offset_for_cardinal_point


def test_part_one():
    assert part_one(1) == 0
    assert part_one(4) == 1
    assert part_one(12) == 3
    assert part_one(15) == 2
    assert part_one(23) == 2
    assert part_one(28) == 3
    assert part_one(34) == 3
    assert part_one(53) == 4
    assert part_one(1024) == 31


def test_get_closest_point():
    assert get_closest_point(12, [11, 15, 19, 23]) == 11


def test_get_cardinal_directions():
    assert get_cardinal_directions(4) == [2, 4, 6, 8]
    assert get_cardinal_directions(5) == [2, 4, 6, 8]
    assert get_cardinal_directions(12) == [11, 15, 19, 23]
    assert get_cardinal_directions(28) == [28, 34, 40, 46]


def test_get_odd_square_below():
    assert get_odd_square_below(4) == 1
    assert get_odd_square_below(9) == 9
    assert get_odd_square_below(12) == 9
    assert get_odd_square_below(24) == 9
    assert get_odd_square_below(28) == 25


def test_offset_for_cardinal_point():
    assert offset_for_cardinal_point(2, get_cardinal_directions(2)) == 1
    assert offset_for_cardinal_point(4, get_cardinal_directions(4)) == 3
    assert offset_for_cardinal_point(11, get_cardinal_directions(11)) == 9
    assert offset_for_cardinal_point(15, get_cardinal_directions(15)) == 11
    assert offset_for_cardinal_point(28, get_cardinal_directions(28)) == 17
    assert offset_for_cardinal_point(34, get_cardinal_directions(34)) == 19
