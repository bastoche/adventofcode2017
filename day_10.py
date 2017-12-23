from functools import reduce


def part_one(input, size=256):
    input_list = map(int, input.split(','))
    elements = list(range(size))
    current_position = 0
    skip_size = 0
    elements, _, _ = run_round(input_list, elements, current_position, skip_size)
    return elements[0] * elements[1]


def run_round(input_list, elements, current_position, skip_size):
    for length in input_list:
        elements = invert_sublist(elements, current_position, length)
        current_position += (length + skip_size) % len(elements)
        skip_size += 1
    return elements, current_position, skip_size


def invert_sublist(elements, start, length):
    for i in range(length // 2):
        swap(elements, (start + i) % len(elements), (start + length - 1 - i) % len(elements))
    return elements


def swap(elements, leftIndex, rightIndex):
    temp = elements[leftIndex]
    elements[leftIndex] = elements[rightIndex]
    elements[rightIndex] = temp
    return elements


def part_two(input, size=256):
    ascii_codes = to_ascii_codes(input)
    sequence = ascii_codes + [17, 31, 73, 47, 23]
    current_position = 0
    skip_size = 0
    elements = list(range(size))
    for i in range(64):
        elements, current_position, skip_size = run_round(sequence, elements, current_position, skip_size)
    dense_hash = to_dense_hash(elements)
    return to_hexadecimal_string(dense_hash)


def to_ascii_codes(input):
    return [ord(character) for character in input]


def to_dense_hash(input):
    length = len(input) // 16
    result = []
    for i in range(length):
        elements = [input[i * 16 + j] for j in range(16)]
        result.append(reduce(lambda a,b: a ^ b, elements))
    return result


def to_hexadecimal_string(input):
    result = ''
    for element in input:
        result += f'{element:02x}'
    return result


if __name__ == "__main__":
    print(part_one('102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216'))
    print(part_two('102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216'))
