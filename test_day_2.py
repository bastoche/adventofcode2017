from day_2 import part_one, max_difference, parse, to_number_list


def test_part_one():
    input = """5 1 9 5
               7 5 3
               2 4 6 8"""
    assert part_one(input) == 18


def test_parse():
    input = """5 1 9 5
               7 5 3
               2 4 6 8"""
    assert parse(input) == [
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8]
    ]


def test_max_difference():
    assert max_difference([5, 1, 9, 5]) == 8
    assert max_difference([7, 5, 3]) == 4
    assert max_difference([2, 4, 6, 8]) == 6


def test_to_number_list():
    assert to_number_list('1 2 3') == [1, 2, 3]
