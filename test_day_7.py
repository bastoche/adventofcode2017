from day_7 import parse_line, part_one, part_two, get_root_program, get_wrong_weight_index, compute_total_weight, Program, find_unbalanced_weight


def test_part_one():
    assert part_one("""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""") == 'tknk'


def test_part_two():
    assert part_two("""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""") == 60


def make_program(name, weight=1, children=[]):
    return Program(name=name, weight=weight, children=children)


def make_programs(programs):
    return {program.name: program for program in programs}


def test_parse_line__without_children():
    program = parse_line("pbga (66)")
    assert program.name == "pbga"
    assert program.weight == 66
    assert program.children == []


def test_parse_line__with_children():
    program = parse_line("fwft (72) -> ktlj, cntj, xhth")
    assert program.name == "fwft"
    assert program.weight == 72
    assert program.children == ["ktlj", "cntj", "xhth"]


def test_get_root_program():
    children = ["abel", "cain"]
    root_program = make_program("root", children=children)
    abel = make_program("abel")
    cain = make_program("cain")
    programs = {
        "root": root_program,
        "abel": abel,
        "cain": cain
    }
    assert get_root_program(programs, children) == root_program


def test_compute_total_weight():
    root_program = make_program("root", children=["abel", "cain"], weight=5)
    abel = make_program("abel", weight=2)
    cain = make_program("cain", weight=3)
    programs = make_programs([root_program, abel, cain])
    assert compute_total_weight(root_program, programs) == 10


def test_get_wrong_weight_index():
    assert get_wrong_weight_index([]) == (-1, 0)
    assert get_wrong_weight_index([1]) == (-1, 0)
    assert get_wrong_weight_index([10, 10, 10]) == (-1, 0)
    assert get_wrong_weight_index([40, 40, 50]) == (2, 40)


def test_find_unbalanced_weight():
    root_program = make_program("root", children=["riri", "fifi", "loulou"], weight=5)
    riri = make_program("riri", weight=2)
    fifi = make_program("fifi", weight=3)
    loulou = make_program("loulou", weight=3)
    programs = make_programs([root_program, riri, fifi, loulou])
    assert not find_unbalanced_weight(riri, programs)
    assert find_unbalanced_weight(root_program, programs) == 3
