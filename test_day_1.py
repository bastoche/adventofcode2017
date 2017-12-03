from day_1 import first_part

def test_first_part():
    assert first_part('1122') == 3
    assert first_part('1111') == 4
    assert first_part('1234') == 0
    assert first_part('91212129') == 9
