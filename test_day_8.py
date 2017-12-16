from collections import defaultdict
from day_8 import part_one, parse_line, process_line, EqualCondition, StrictlySuperiorCondition, StrictlyInferiorCondition, SuperiorCondition, IncrementOperation, DecrementOperation


def test_part_one():
    assert part_one("""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""") == 1


def test_parse_line():
    assert parse_line('b inc 5 if a > 1') == (StrictlySuperiorCondition('a', 1), IncrementOperation('b', 5))
    assert parse_line('a inc 1 if b < 5') == (StrictlyInferiorCondition('b', 5), IncrementOperation('a', 1))
    assert parse_line('c dec -10 if a >= 1') == (SuperiorCondition('a', 1), DecrementOperation('c', -10))
    assert parse_line('c inc -20 if c == 10') == (EqualCondition('c', 10), IncrementOperation('c', -20))


def test_process_line():
    registers = defaultdict(int)
    process_line('b inc 5 if a > 1', registers)
    assert registers['b'] == 0
    process_line('a inc 1 if b < 5', registers)
    assert registers['a'] == 1
