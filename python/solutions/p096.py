def import_sudoku(path: str) -> list[list[list[int]]]:
    all_grids = []
    current_grid: list[list[int]] = []
    with open(path, "r") as f:
        for line in f:
            if "Grid" in line:
                if current_grid:
                    all_grids.append(current_grid)
                    current_grid = []
                continue

            row = [int(x) for x in line.strip()]
            current_grid.append(row)
        all_grids.append(current_grid)
        return all_grids


def is_valid(sudoku: list[list[int]], row: int, col: int, number: int) -> bool:
    for i in range(9):
        # Checks number in same row
        if sudoku[row][i] == number:
            return False
        # Checks valid in same column
        if sudoku[i][col] == number:
            return False
        relative_row = (row // 3) * 3
        relative_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + relative_row][j + relative_col] == number:
                return False
    return True


def solve_sudoku(sudoku: list[list[int]]) -> bool:
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True


def solve(sudoku_list: list[list[list[int]]]) -> int:
    solution = 0
    for sudoko in sudoku_list:
        solve_sudoku(sudoko)
        solution += sudoko[0][0] * 100 + sudoko[0][1] * 10 + sudoko[0][2]
    return solution


if __name__ == "__main__":
    print(solve(import_sudoku("inputs/096_sudoku.txt")))
