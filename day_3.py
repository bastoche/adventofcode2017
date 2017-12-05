import math


def part_one(input):
    if input == 1:
        return 0

    points = get_cardinal_directions(input)

    if input in points:
        return 1 + part_one(input - offset_for_cardinal_point(input, points))

    closest_point = get_closest_point(input, points)
    if input < closest_point:
        return 1 + part_one(input + 1)
    else:
        return 1 + part_one(input - 1)


def get_closest_point(input, points):
    return min(points, key=lambda x: abs(x - input))


def get_cardinal_directions(input):
    odd_square_below = get_odd_square_below(input)
    odd_square_above = (math.sqrt(odd_square_below) + 2) * (math.sqrt(odd_square_below) + 2)
    steps = (odd_square_above - odd_square_below) // 4
    east = odd_square_below + steps // 2
    north = east + steps
    west = north + steps
    south = west + steps
    return [east, north, west, south]


def get_odd_square_below(input):
    root = math.floor(math.sqrt(input))
    if root % 2 == 0:
        root = root - 1
    return root * root


def offset_for_cardinal_point(input, points):
    side_length_for_previous_square = math.sqrt(get_odd_square_below(input)) - 1
    return side_length_for_previous_square * 4 + 1 + points.index(input) * 2


if __name__ == "__main__":
    input = 325489
    print(part_one(input))
