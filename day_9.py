def part_one(input):
    score, _ = process_input(input)
    return score


def part_two(input):
    _, cleaned_garbage = process_input(input)
    return cleaned_garbage


def process_input(input):
    score = 0
    cleaned_garbage = 0
    depth = 0
    garbage = False
    cancel = False
    for char in input:
        if cancel:
            cancel = False
            continue
        elif char == '!':
            cancel = True
        elif char == '>':
            garbage = False
        elif garbage:
            cleaned_garbage += 1
            continue
        elif char == '<':
            garbage = True
        elif char == '{':
            depth += 1
        elif char == '}':
            score += depth
            depth -= 1
    return score, cleaned_garbage


if __name__ == "__main__":
    with open('day_9.txt') as file:
        input = file.read()
    print(part_one(input))
    print(part_two(input))
