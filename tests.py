import pytest

from iin_validation import validate_iin


@pytest.mark.parametrize(
    "iin, expected",
    [
        ("990425400461", True),
        ("304212233", False),
        ("112233445566", False),
    ],
)
def test_validate_iin(iin, expected):
    assert validate_iin(iin) == expected
