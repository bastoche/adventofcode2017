from day_4 import part_one, is_valid


def test_part_one():
    assert part_one("""aa bb cc dd ee
                       aa bb cc dd aa
                       aa bb cc dd aaa""") == 2


def test_is_valid():
    assert(is_valid('aa bb cc dd ee')) == True
    assert(is_valid('aa bb cc dd aa')) == False
    assert(is_valid('aa bb cc dd aaa')) == True
