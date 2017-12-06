from math import ceil, sqrt


def part_one(input):
    circle_index = get_circle_index(input)
    circle_zero = get_circle_zero(circle_index)
    cardinal_points = get_cardinal_points(circle_index, circle_zero)
    distance_to_closest_cardinal_point = compute_distance_to_closest_cardinal_point(input, cardinal_points)
    return circle_index + distance_to_closest_cardinal_point


def get_circle_index(input):
    return ceil(sqrt(input)) // 2


def get_circle_zero(circle_index):
    return pow(circle_index * 2 - 1, 2)


def get_cardinal_points(circle_index, circle_zero):
    return [circle_zero + x * circle_index for x in [1, 3, 5, 7]]


def compute_distance_to_closest_cardinal_point(input, cardinal_points):
    return min([abs(input - x) for x in cardinal_points])


if __name__ == "__main__":
    input = 325489
    print(part_one(input))
