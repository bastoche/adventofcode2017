from day_9 import part_one


def test_part_one():
    assert part_one('{}') == 1
    assert part_one('{{{}}}') == 6
    assert part_one('{{},{}}') == 5
    assert part_one('{{{},{},{{}}}}') == 16
    assert part_one('{<a>,<a>,<a>,<a>}') == 1
    assert part_one('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert part_one('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert part_one('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3
