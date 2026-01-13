from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

Cell = Union[int, str]


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Cell]]:
    return [["■" for _ in range(cols)] for _ in range(rows)]


def remove_wall(grid: List[List[Cell]], pos: Tuple[int, int]) -> List[List[Cell]]:
    r, c = pos
    max_r, max_c = len(grid), len(grid[0])

    dr, dc = (-2, 0) if choice((True, False)) else (0, 2)
    nr, nc = r + dr, c + dc

    if not (0 <= nr < max_r and 0 <= nc < max_c):
        dr, dc = (0, 2) if dr != 0 else (-2, 0)
        nr, nc = r + dr, c + dc
        if not (0 <= nr < max_r and 0 <= nc < max_c):
            return grid

    wr = r - 1 if nr < r else r
    wc = c + 1 if nc > c else c
    grid[wr][wc] = " "
    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Cell]]:
    grid = create_grid(rows, cols)
    candidates = []

    for i in range(rows):
        for j in range(cols):
            if (i & 1) and (j & 1):
                grid[i][j] = " "
                candidates.append((i, j))

    for coord in candidates:
        remove_wall(grid, coord)

    if random_exit:
        t, b = randint(0, rows - 1), randint(0, rows - 1)
        y1 = randint(0, cols - 1) if t in (0, rows - 1) else choice((0, cols - 1))
        y2 = randint(0, cols - 1) if b in (0, rows - 1) else choice((0, cols - 1))
    else:
        t, y1 = 0, cols - 2
        b, y2 = rows - 1, 1

    grid[t][y1] = grid[b][y2] = "X"
    return grid


def get_exits(grid: List[List[Cell]]) -> List[Tuple[int, int]]:
    return [(i, j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == "X"]


def make_step(grid: List[List[Cell]], k: int) -> List[List[Cell]]:
    h, w = len(grid), len(grid[0])
    for i in range(h):
        for j in range(w):
            if grid[i][j] == k:
                for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 0:
                        grid[ni][nj] = k + 1
    return grid


def encircled_exit(grid: List[List[Cell]], pos: Tuple[int, int]) -> bool:
    r, c = pos
    h, w = len(grid), len(grid[0])

    if r not in (0, h - 1) and c not in (0, w - 1):
        return False

    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != "■":
            return False
    return True


def shortest_path(grid, exit_coord):
    rows = len(grid)
    cols = len(grid[0])

    x, y = exit_coord
    cell = grid[x][y]

    if not isinstance(cell, int) or cell <= 1:
        return None

    value = cell
    path = [(x, y)]

    while value > 1:
        moved = False
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbour = grid[nx][ny]
                if isinstance(neighbour, int) and neighbour == value - 1:
                    path.append((nx, ny))
                    x, y = nx, ny
                    value -= 1
                    moved = True
                    break

        if not moved:
            return None

    return path


def solve_maze(grid: List[List[Cell]]) -> Tuple[List[List[Cell]], Optional[List[Tuple[int, int]]]]:
    maze = deepcopy(grid)
    exits = get_exits(maze)

    if len(exits) < 2 or any(encircled_exit(maze, e) for e in exits):
        return maze, None

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] in (" ", "X"):
                maze[i][j] = 0

    start, finish = exits
    maze[start[0]][start[1]] = 1

    step = 1
    while maze[finish[0]][finish[1]] == 0:
        prev = deepcopy(maze)
        make_step(maze, step)
        if prev == maze:
            break
        step += 1

    if maze[finish[0]][finish[1]] == 0:
        return maze, None
    return maze, shortest_path(maze, finish)


def add_path_to_grid(grid: List[List[Cell]], path: Optional[List[Tuple[int, int]]]) -> List[List[Cell]]:
    if path:
        for r, c in path:
            grid[r][c] = "X"
    return grid


def print_grid(grid: List[List[Cell]]) -> None:
    print("\n".join(" ".join(str(c) for c in row) for row in grid))


if __name__ == "__main__":
    g = bin_tree_maze()
    print_grid(g)
    solved, route = solve_maze(g)
    print()
    print_grid(add_path_to_grid(solved, route))
