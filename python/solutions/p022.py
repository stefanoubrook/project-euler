def load_names(path: str) -> list[str]:
    """Reads the file, strips quotes and returns a sorted list of names"""
    with open(path, "r") as f:
        data = f.read()
        data = data.replace('"', "")
        names = data.split(",")
        ordered_names = sorted(names)

        return ordered_names


def name_score(name: str, index: int) -> int:
    score = 0
    for letter in name:
        score += ord(letter) - 64
    score *= index
    return score


def solve(names: list[str]) -> int:
    total_score = 0
    for i, name in enumerate(names):
        total_score += name_score(name, i + 1)

    return total_score


if __name__ == "__main__":
    print(solve(load_names("inputs/022_names.txt")))
