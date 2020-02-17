from typing import List


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
