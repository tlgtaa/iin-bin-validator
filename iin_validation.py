"""
Based on a control digit calculation formula described in wikipedia.

https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D0%B4%D0%B8%D0%B2%D0%B8%D0%B4%D1%83%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%B8%D0%B4%D0%B5%D0%BD%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BD%D0%BE%D0%BC%D0%B5%D1%80#%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D0%98%D0%98%D0%9D
"""

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
