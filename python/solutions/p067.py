def load_integers(path: str) -> list[list[int]]:
    with open(path, "r") as f:
        triangle = [list(map(int, line.split())) for line in f]
        return triangle


def solve(triangle: list[list[int]]) -> int:
    for i in reversed(range(len(triangle))):
        for j in range(len(triangle[i]) - 1):
            if i != len(triangle):
                triangle[i - 1][j] += max(triangle[i][j], triangle[i][j + 1])
    return triangle[0][0]


if __name__ == "__main__":
    print(solve(load_integers("inputs/067_triangle.txt")))
