def solve(n: int) -> int:
    coin_types: list[int] = [1, 2, 5, 10, 20, 50, 100, 200]
    # Initialise dictionary with 0 ways set as default
    ways_to_get_to: dict[int, int] = {i: 0 for i in range(1, n + 1)}
    for coin in coin_types:
        if coin <= n:
            ways_to_get_to[coin] += 1
        for i in range(coin, n + 1):
            if i - coin > 0:
                ways_to_get_to[i] += ways_to_get_to[i - coin]
    return ways_to_get_to[n]


if __name__ == "__main__":
    print(solve(200))
