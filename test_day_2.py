from day_2 import part_one, max_difference, parse, to_number_list, part_two, even_division_result, all_pairs, max_even_division_result


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


def test_part_two():
    input = """5 9 2 8
               9 4 7 3
               3 8 6 5"""
    assert part_two(input) == 9


def test_even_division_result():
    assert even_division_result(2, 4) == 2
    assert even_division_result(2, 5) == 0


def test_all_pairs():
    assert all_pairs([]) == []
    assert all_pairs(sorted([1, 2, 3])) == sorted([(1, 2), (2, 3), (1, 3)])


def test_max_even_division_result():
    assert max_even_division_result(all_pairs([5, 9, 2, 8])) == 4
