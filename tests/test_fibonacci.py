from typing import List

import pytest

from fibonacci import fibonacci


@pytest.mark.parametrize(
    'max_value,expected',
    [
        (0, [0]),
        (1, [0, 1, 1]),
        (2, [0, 1, 1, 2]),
        (3, [0, 1, 1, 2, 3]),
        (4, [0, 1, 1, 2, 3]),
        (5, [0, 1, 1, 2, 3, 5]),
    ]
)
def test_fibonacci(max_value: int, expected: List[int]):
    assert fibonacci(max_value) == expected


def test_fibonacci_negative_value():
    with pytest.raises(ValueError) as e:
        fibonacci(-1)

    assert "Fibonacci sequence doesn't contain negative values" in str(e.value)
