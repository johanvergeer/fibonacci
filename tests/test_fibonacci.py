from typing import List

import pytest

from fibonacci import fibonacci_up_to


@pytest.mark.parametrize(
    "max_value,expected",
    [
        (0, [0]),
        (1, [0, 1, 1]),
        (2, [0, 1, 1, 2]),
        (3, [0, 1, 1, 2, 3]),
        (4, [0, 1, 1, 2, 3]),
        (5, [0, 1, 1, 2, 3, 5]),
    ],
)
def test_fibonacci_up_to(max_value: int, expected: List[int]) -> None:
    assert fibonacci_up_to(max_value) == expected


def test_fibonacci_up_to_negative_value() -> None:
    with pytest.raises(ValueError) as e:
        fibonacci_up_to(-1)

    assert "Fibonacci sequence doesn't contain negative values" in str(e.value)
