def part_one(input, size=256):
    input_list = map(int, input.split(','))
    elements = list(range(0, size))
    start = 0
    skip_size = 0
    for length in input_list:
        elements = invert_sublist(elements, start, length)
        start += (length + skip_size) % len(elements)
        skip_size += 1
    return elements[0] * elements[1]


def invert_sublist(elements, start, length):
    for i in range(0, length // 2):
        swap(elements, (start + i) % len(elements), (start + length - 1 - i) % len(elements))
    return elements


def swap(elements, leftIndex, rightIndex):
    temp = elements[leftIndex]
    elements[leftIndex] = elements[rightIndex]
    elements[rightIndex] = temp
    return elements


if __name__ == "__main__":
    print(part_one('102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216'))
