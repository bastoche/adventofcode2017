from day_4 import part_one, contains_only_unique_elements, contains_anagrams


def test_part_one():
    assert part_one("""aa bb cc dd ee
                       aa bb cc dd aa
                       aa bb cc dd aaa""") == 2


def test_contains_only_unique_elements():
    assert contains_only_unique_elements('aa bb cc dd ee')
    assert not contains_only_unique_elements('aa bb cc dd aa')
    assert contains_only_unique_elements('aa bb cc dd aaa')


def test_contains_anagrams():
    assert not contains_anagrams('abcde fghij')
    assert contains_anagrams('abcde xyz ecdab')
    assert not contains_anagrams('a ab abc abd abf abj')
    assert not contains_anagrams('iiii oiii ooii oooi oooo')
    assert contains_anagrams('oiii ioii iioi iiio')
