def limit_size(size, expected_size):
    return expected_size if size >= expected_size else size


def full_range(start, end):
    return range(start, end + 1)


def full_array_range(array):
    return range(array[0], array[1] + 1)
