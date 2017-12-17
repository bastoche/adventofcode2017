def part_one(input):
    score = 0
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
            continue
        elif char == '<':
            garbage = True
        elif char == '{':
            depth += 1
        elif char == '}':
            score += depth
            depth -= 1
    return score


if __name__ == "__main__":
    with open('day_9.txt') as file:
        input = file.read()
    print(part_one(input))
