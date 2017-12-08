def part_one(input):
    iterations = 0
    seen_states = set()
    state = string_to_integer_list(input)
    while integer_list_to_string(state) not in seen_states:
        seen_states.add(integer_list_to_string(state))
        state = redistribute(state)
        iterations += 1
    return iterations


def redistribute(list):
    max_value = max(list)
    max_index = list.index(max_value)
    list[max_index] = 0
    for i in range(max_value):
        index = (max_index + i + 1) % len(list)
        list[index] += 1
    return list


def string_to_integer_list(string):
    return list(map(int, string.split()))


def integer_list_to_string(integer_list):
    return ' '.join(map(str, integer_list))


def part_two(input):
    iterations = 0
    seen_states = {}
    state = string_to_integer_list(input)
    while integer_list_to_string(state) not in seen_states:
        seen_states[integer_list_to_string(state)] = iterations
        state = redistribute(state)
        iterations += 1
    return iterations - seen_states[integer_list_to_string(state)]


if __name__ == "__main__":
    input = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"
    print(part_one(input))
    print(part_two(input))
