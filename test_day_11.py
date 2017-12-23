from collections import defaultdict
from day_11 import part_one, to_frequency_dict, cancel_directions, transform_directions, part_two


def test_part_one():
    assert part_one('ne,ne,ne') == 3
    assert part_one('ne,ne,sw,sw') == 0
    assert part_one('ne,ne,s,s') == 2
    assert part_one('se,sw,se,sw,sw') == 3


def test_to_frequency_dict():
    assert to_frequency_dict(['se', 'ne', 'se']) == {'ne': 1, 'se': 2}


def test_cancel_directions():
    assert cancel_directions(defaultdict(int, {'ne': 1, 'sw': 2}), 'ne', 'sw') == {'ne': 0, 'sw': 1}


def test_transform_directions():
    assert transform_directions(defaultdict(int, {'ne': 2, 's': 1}), 'ne', 's', 'se') == {'ne': 1, 's': 0, 'se': 1}


def test_part_two():
    assert part_two('ne,ne,ne') == 3
    assert part_two('ne,ne,sw,sw') == 2
    assert part_two('ne,ne,s,s') == 2
    assert part_two('se,sw,se,sw,sw') == 3
