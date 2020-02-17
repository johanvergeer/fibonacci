from typing import List


def fibonacci_sequence(values_count: int) -> List[int]:
    """Creates a Fibonacci sequences`

    Args:
        values_count: Number of values in the calculated sequence

    Returns:
        Fibonacci sequence

    Examples:
        >>> fibonacci_sequence(1)
        [0]

        >>> fibonacci_sequence(2)
        [0, 1]

        >>> fibonacci_sequence(5)
        [0, 1, 1, 2, 3]

    """
    if values_count <= 0:
        raise ValueError("values_count must be greater than 0")

    sequence: List[int] = []

    for i in range(1, values_count + 1):
        if i == 1:
            sequence.append(0)
        elif i == 2:
            sequence.append(1)
        else:
            sequence.append(sequence[-1] + sequence[-2])

    return sequence


def fibonacci_up_to(max_value: int) -> List[int]:
    """Calculates a Fibonacci sequence up to :param:`max_value`

    Args:
        max_value: Maximum value in the Fibonacci sequence

    Returns:
        Fibonacci sequence

    Examples:
        >>> fibonacci_up_to(0)
        [0]

        >>> fibonacci_up_to(5)
        [0, 1, 1, 2, 3, 5]
    """
    if max_value < 0:
        raise ValueError("Fibonacci sequence doesn't contain negative values")

    sequence: List[int] = [0, 1, 1]

    if max_value == 0:
        return [0]
    elif max_value == 1:
        return sequence

    while True:
        next_: int = sequence[-1] + sequence[-2]
        if next_ > max_value:
            return sequence
        sequence.append(next_)
