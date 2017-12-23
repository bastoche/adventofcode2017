from day_10 import part_one, invert_sublist, swap, part_two, to_ascii_codes, to_dense_hash, to_hexadecimal_string


def test_part_one():
    assert part_one('3,4,1,5', size=5) == 12


def test_invert_sublist():
    assert invert_sublist([0, 1, 2, 3, 4], 0, 3) == [2, 1, 0, 3, 4]
    assert invert_sublist([2, 1, 0, 3, 4], 3, 4) == [4, 3, 0, 1, 2]
    assert invert_sublist([4, 3, 0, 1, 2], 3, 1) == [4, 3, 0, 1, 2]
    assert invert_sublist([4, 3, 0, 1, 2], 1, 5) == [3, 4, 2, 1, 0]


def test_swap():
    assert swap([0, 1, 2, 3, 4], 0, 2) == [2, 1, 0, 3, 4]


def test_part_two():
    assert part_two('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert part_two('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert part_two('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert part_two('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'


def test_to_ascii_codes():
    assert to_ascii_codes('1,2,3') == [49, 44, 50, 44, 51]


def test_to_dense_hash():
    assert to_dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == [64]
    assert to_dense_hash([0] * 256) == [0] * 16
    assert to_dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22] * 16) == [64] * 16


def test_to_hexadecimal_string():
    assert to_hexadecimal_string([64, 7, 255]) == '4007ff'
