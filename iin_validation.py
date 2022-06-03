import re


def validate_iin(iin: str) -> bool:

    if not re.match(r"[0-9]{12}", iin):
        return False

    iin_digits_as_int = list(map(int, iin))
    weights = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
    control_digit = _calculate_control_digit(iin_digits_as_int, weights)
    if control_digit == 10:
        weights = {3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2}
        control_digit = _calculate_control_digit(iin_digits_as_int)

    return control_digit == iin_digits_as_int[-1]


def _calculate_control_digit(iin_digits: list[int], weights: set[int]) -> int:
    # in the zip method, the iterator stops when the shortest iterable is exhausted.
    # so last number of iin will be ignored

    return sum([weight * digit for weight, digit in zip(weights, iin_digits)]) % 11
