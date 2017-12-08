def part_one(input):
    iterations = 0
    seen_states = set()
    state = list(map(int, input.split()))
    while True:
        iterations += 1
        seen_states.add(' '.join(map(str, state)))
        state = redistribute(state)
        if ' '.join(map(str, state)) in seen_states:
            break
    return iterations


def redistribute(list):
    max_value = max(list)
    max_index = list.index(max_value)
    list[max_index] = 0
    for i in range(max_value):
        index = (max_index + i + 1) % len(list)
        list[index] += 1
    return list


if __name__ == "__main__":
    input = "4	1	15	12	0	9	9	5	5	8	7	3	14	5	12	3"
    print(part_one(input))
