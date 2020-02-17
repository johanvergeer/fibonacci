from typing import List

import pytest

from fibonacci import fibonacci_sequence, fibonacci_up_to, fibonacci_value


def test_fibonacci_value__0():
    assert fibonacci_value(0) == 0


def test_fibonacci_value__1():
    assert fibonacci_value(1) == 1


def test_fibonacci_value__75():
    assert fibonacci_value(75) == 2111485077978055


def test_fibonacci_sequence__values_count_0():
    with pytest.raises(ValueError) as e:
        fibonacci_sequence(0)

    assert "values_count must be greater than 0" in str(e.value)


def test_fibonacci_sequence__values_count__smaller_than_0():
    with pytest.raises(ValueError) as e:
        fibonacci_sequence(-1)

    assert "values_count must be greater than 0" in str(e.value)


def test_fibonacci_sequence__values_count__1():
    assert fibonacci_sequence(1) == [0]


def test_fibonacci_sequence__values_count__2():
    assert fibonacci_sequence(2) == [0, 1]
    assert fibonacci_sequence(1) == [0]


def test_fibonacci_sequence__values_count__3():
    assert fibonacci_sequence(3) == [0, 1, 1]


def test_fibonacci_sequence__values_count__4():
    assert fibonacci_sequence(4) == [0, 1, 1, 2]


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
