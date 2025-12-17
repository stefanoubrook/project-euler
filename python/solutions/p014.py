import functools


@functools.cache
def get_collatz_length(n: int) -> int:
    """Returns the length of the Collatz chain starting at n.
    Uses memoization to avoid re-calculating known chains."""

    if n == 1:
        return 1

    if n % 2 == 0:
        next_n = n // 2
    else:
        next_n = 3 * n + 1
    return 1 + get_collatz_length(next_n)


def solve(limit: int) -> int:
    """Finds the starting number under 'limit' that provides the longest chain"""
    max_length = 0
    answer = 1

    for i in range(1, limit):
        length = get_collatz_length(i)
        if length > max_length:
            max_length = length
            answer = i

    return answer


if __name__ == "__main__":
    print(solve(1_000_000))
