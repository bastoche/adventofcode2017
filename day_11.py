from collections import defaultdict


def part_one(input):
    directions_list = input.split(',')
    directions_dict = to_frequency_dict(directions_list)
    directions_dict = cancel_opposite_directions(directions_dict)
    directions_dict = find_shortcuts(directions_dict)
    return sum([value for key,value in directions_dict.items()])


def to_frequency_dict(word_list):
    result = defaultdict(int)
    for word in word_list:
        result[word] += 1
    return result


def cancel_opposite_directions(directions_dict):
    directions_dict = cancel_directions(directions_dict, 'n', 's')
    directions_dict = cancel_directions(directions_dict, 'ne', 'sw')
    directions_dict = cancel_directions(directions_dict, 'e', 'w')
    directions_dict = cancel_directions(directions_dict, 'se', 'nw')
    return directions_dict


def cancel_directions(directions_dict, left, right):
    left_count = directions_dict[left]
    right_count = directions_dict[right]
    cancel_count = min(left_count, right_count)
    directions_dict[left] = max(left_count - cancel_count, 0)
    directions_dict[right] = max(right_count - cancel_count, 0)
    return directions_dict


def find_shortcuts(directions_dict):
    directions_dict = transform_directions(directions_dict, 'ne', 's', 'se')
    directions_dict = transform_directions(directions_dict, 'se', 'sw', 's')
    directions_dict = transform_directions(directions_dict, 's', 'nw', 'sw')
    directions_dict = transform_directions(directions_dict, 'sw', 'n', 'nw')
    directions_dict = transform_directions(directions_dict, 'nw', 'ne', 'n')
    directions_dict = transform_directions(directions_dict, 'n', 'se', 'ne')
    return directions_dict


def transform_directions(directions_dict, left, right, result):
    left_count = directions_dict[left]
    right_count = directions_dict[right]
    cancel_count = min(left_count, right_count)
    directions_dict[left] = max(left_count - cancel_count, 0)
    directions_dict[right] = max(right_count - cancel_count, 0)
    directions_dict[result] += cancel_count
    return directions_dict


if __name__ == "__main__":
    with open('day_11.txt') as file:
        input = file.read()
    print(part_one(input))
