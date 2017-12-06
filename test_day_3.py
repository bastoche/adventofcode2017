from day_3 import part_one, get_circle_index, get_circle_zero, get_cardinal_points, compute_distance_to_closest_cardinal_point, part_two, get_next_coordinates


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


def test_compute_distance_to_closest_cardinal_point():
    assert compute_distance_to_closest_cardinal_point(12, [11, 15, 19, 23]) == 1
    assert compute_distance_to_closest_cardinal_point(21, [11, 15, 19, 23]) == 2


def test_get_cardinal_points():
    assert get_cardinal_points(1, 1) == [2, 4, 6, 8]
    assert get_cardinal_points(2, 9) == [11, 15, 19, 23]
    assert get_cardinal_points(3, 25) == [28, 34, 40, 46]


def test_get_circle_index():
    assert get_circle_index(4) == 1
    assert get_circle_index(9) == 1
    assert get_circle_index(11) == 2
    assert get_circle_index(15) == 2
    assert get_circle_index(28) == 3


def test_get_circle_zero():
    assert get_circle_zero(2) == 9
    assert get_circle_zero(3) == 25
    assert get_circle_zero(4) == 49


def test_part_two():
    assert part_two(6) == 10
    assert part_two(30) == 54


def test_get_next_coordinates():
    get_next_coordinates(0, 0) == (1, 0)
    get_next_coordinates(0, 1) == (1, 1)
    get_next_coordinates(1, 1) == (0, 1)
    get_next_coordinates(0, 1) == (-1, 1)
    get_next_coordinates(-1, 1) == (-1, 0)
    get_next_coordinates(-1, 0) == (-1, -1)
    get_next_coordinates(-1, -1) == (0, -1)
    get_next_coordinates(0, -1) == (1, -1)
    get_next_coordinates(1, -1) == (2, -1)
