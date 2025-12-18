def load_triangles(path: str) -> list[list[int]]:
    with open(path, "r") as f:
        data: str = f.read()
        triangle_data: list[list[int]] = [
            [int(x) for x in line.split(",")] for line in data.splitlines()
        ]
        return triangle_data


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repn__(self):
        return f"Point({self.x},{self.y})"

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def det(self, other):
        return (self.x * other.y) - (self.y * other.x)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def __repn__(self):
        return f"Triangle({self.a},{self.b},{self.c})"

    @classmethod
    def from_row(cls, row: list[int]):
        p1 = Point(row[0], row[1])
        p2 = Point(row[2], row[3])
        p3 = Point(row[4], row[5])
        return cls(p1, p2, p3)


def solve(triangle_data: list[list[int]]) -> int:
    origin = Point(0, 0)
    answer = 0
    for row in triangle_data:
        T = Triangle.from_row(row)
        # creates vectors XY from X to Y
        AB = T.b - T.a
        BC = T.c - T.b
        CA = T.a - T.c
        # calculates the determinant of XY | OX. If > 0 point on left
        d1 = AB.det(origin - T.a)
        d2 = BC.det(origin - T.b)
        d3 = CA.det(origin - T.c)
        if (d1 * d2) > 0 and (d2 * d3 > 0):
            answer += 1
    return answer


if __name__ == "__main__":
    print(solve(load_triangles("inputs/102_triangles.txt")))
