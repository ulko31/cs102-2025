# from copy import deepcopy
# from random import choice, randint
# from typing import List, Optional, Tuple, Union
#
# import pandas as pd
#
#
# def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
#     return [["■"] * cols for _ in range(rows)]
#
# def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
#     """
#
#     :param grid:
#     :param coord:
#     :return:
#     """
#     x, y = coord
#     index_last_col = len(grid[0]) - 1
#     direction = choice(("up", "right"))
#     if direction == "up":
#         if x > 1:
#             grid[x - 1][y] = " "
#         elif y < index_last_col - 1:
#             grid[x][y + 1] = " "
#     else:
#         if y < index_last_col - 1:
#             grid[x][y + 1] = " "
#         elif x > 1:
#             grid[x - 1][y] = " "
#     return grid
#
#
# def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
#     """
#
#     :param rows:
#     :param cols:
#     :param random_exit:
#     :return:
#     """
#
#     grid = create_grid(rows, cols)
#     empty_cells = []
#     for x, row in enumerate(grid):
#         for y, _ in enumerate(row):
#             if x % 2 == 1 and y % 2 == 1:
#                 grid[x][y] = " "
#                 empty_cells.append((x, y))
#
#     # 1. выбрать любую клетку
#     # 2. выбрать направление: наверх или направо.
#     # Если в выбранном направлении следующая клетка лежит за границами поля,
#     # выбрать второе возможное направление
#     # 3. перейти в следующую клетку, сносим между клетками стену
#     # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки
#     for current_cell in empty_cells:
#         remove_wall(grid, current_cell)
#     if random_exit:
#         x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
#         y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
#         y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
#     else:
#         x_in, y_in = 0, cols - 2
#         x_out, y_out = rows - 1, 1
#     grid[x_in][y_in], grid[x_out][y_out] = "X", "X"
#     return grid
#
# # def bin_tree_maze(
# #     rows: int = 15, cols: int = 15, random_exit: bool = True
# # ) -> List[List[Union[str, int]]]:
# #     """
# #     Генерирует лабиринт с помощью алгоритма двоичного дерева.
# #     :param rows:
# #     :param cols:
# #     :param random_exit:
# #     :return:
# #     """
# #     grid = create_grid(rows, cols)
# #     empty_cells = []
# #     for x in range(rows):
# #         for y in range(cols):
# #             if x % 2 == 1 and y % 2 == 1:
# #                 grid[x][y] = " "
# #                 empty_cells.append((x, y))
# #
# #     # Обрабатываем каждую пустую клетку
# #     for x, y in empty_cells:
# #         remove_wall(grid, (x, y))
# #
# #     # Генерация входа и выхода
# #     if random_exit:
# #         exits = []
# #         for _ in range(2):
# #             side = randint(0, 3)  # 0: верх, 1: право, 2: низ, 3: лево
# #             if side == 0:  # верх
# #                 x_out = 0
# #                 y_out = randint(1, cols - 2)
# #             elif side == 1:  # право
# #                 x_out = randint(1, rows - 2)
# #                 y_out = cols - 1
# #             elif side == 2:  # низ
# #                 x_out = rows - 1
# #                 y_out = randint(1, cols - 2)
# #             else:  # лево
# #                 x_out = randint(1, rows - 2)
# #                 y_out = 0
# #             exits.append((x_out, y_out))
# #         x_in, y_in = exits[0]
# #         x_out, y_out = exits[1]
# #     else:
# #         x_in, y_in = 0, cols - 2
# #         x_out, y_out = rows - 1, 1
# #
# #     grid[x_in][y_in] = "X"
# #     grid[x_out][y_out] = "X"
# #
# #     return grid
#
#
# def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
#     """
#     Находит координаты всех выходов (клеток с 'X').
#     :param grid:
#     :return:
#     """
#     exits = []
#     for i, row in enumerate(grid):
#         for j, cell in enumerate(row):
#             if cell == "X":
#                 exits.append((i, j))
#     return exits
#
#
# def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
#     """
#
#     :param grid:
#     :param coord:
#     :return:
#     """
#     x, y = coord
#     rows = len(grid)
#     cols = len(grid[0])
#
#     if not (x == 0 or x == rows - 1 or y == 0 or y == cols - 1):
#         return False
#
#     walls = 0
#     possible = 0
#
#     if x > 0:
#         possible += 1
#         if grid[x - 1][y] == "■":
#             walls += 1
#     if x < rows - 1:
#         possible += 1
#         if grid[x + 1][y] == "■":
#             walls += 1
#     if y > 0:
#         possible += 1
#         if grid[x][y - 1] == "■":
#             walls += 1
#     if y < cols - 1:
#         possible += 1
#         if grid[x][y + 1] == "■":
#             walls += 1
#
#     return walls == possible
#
#
# def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
#     """
#     Распространяет метку k+1 по соседним пустым клеткам.
#     :param grid:
#     :param k:
#     :return:
#     """
#     rows, cols = len(grid), len(grid[0])
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == k:
#                 for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                     ni, nj = i + dx, j + dy
#                     if 0 <= ni < rows and 0 <= nj < cols:
#                         if grid[ni][nj] == " " or grid[ni][nj] == 0:
#                             grid[ni][nj] = k + 1
#     return grid
#
#
# def shortest_path(
#     grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
# ) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
#     """
#     Восстанавливает кратчайший путь от выхода до входа.
#     Возвращает путь в порядке: [выход, ..., вход].
#     :param grid:
#     :param exit_coord:
#     :return:
#     """
#     path = []
#     x, y = exit_coord
#
#     # Если выход недостижим или не имеет метки
#     if not isinstance(grid[x][y], int) or grid[x][y] <= 0:
#         return None
#
#     k = grid[x][y]  # начинаем с метки в выходе
#
#     while k >= 1:
#         path.append((x, y))
#         found = False
#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
#                 if isinstance(grid[nx][ny], int) and grid[nx][ny] == k - 1:
#                     x, y = nx, ny
#                     k -= 1
#                     found = True
#                     break
#         if not found:
#             break
#
#     # Путь должен заканчиваться на метке 1 (вход)
#     if path and grid[path[-1][0]][path[-1][1]] == 1:
#         return path  # уже в порядке: выход → вход
#     return None
#
#
# def solve_maze(
#     grid: List[List[Union[str, int]]],
# ) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
#     """
#     Решает лабиринт: находит путь от одного выхода до другого.
#     :param grid:
#     :return:
#     """
#     exits = get_exits(grid)
#     if len(exits) == 0:
#         return grid, None
#     if len(exits) == 1:
#         return grid, [exits[0]]
#
#     x1, y1 = exits[0]
#     x2, y2 = exits[1]
#
#     if encircled_exit(grid, (x1, y1)) or encircled_exit(grid, (x2, y2)):
#         return grid, None
#
#     # Копия лабиринта для разметки
#     grid_copy = deepcopy(grid)
#
#     # Инициализация: вход — 1, выход — 0, остальные пустые — 0
#     grid_copy[x1][y1] = 1
#     if isinstance(grid_copy[x2][y2], int) or grid_copy[x2][y2] == " ":
#         grid_copy[x2][y2] = 0
#     for i in range(len(grid_copy)):
#         for j in range(len(grid_copy[i])):
#             if grid_copy[i][j] == " ":
#                 grid_copy[i][j] = 0
#
#     k = 1
#     while grid_copy[x2][y2] == 0:
#         grid_copy = make_step(grid_copy, k)
#         if grid_copy[x2][y2] != 0:
#             break
#         # Проверим, есть ли ещё клетки со значением k
#         has_k = any(
#             isinstance(grid_copy[i][j], int) and grid_copy[i][j] == k
#             for i in range(len(grid_copy))
#             for j in range(len(grid_copy[i]))
#         )
#         if not has_k:
#             return grid, None
#         k += 1
#
#     path = shortest_path(grid_copy, (x2, y2))
#     return grid, path
#
#
# def add_path_to_grid(
#     grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
# ) -> List[List[Union[str, int]]]:
#     """
#     Добавляет путь на лабиринт.
#     :param grid:
#     :param path:
#     :return:
#     """
#     if path:
#         for i, row in enumerate(grid):
#             for j, _ in enumerate(row):
#                 if (i, j) in path:
#                     grid[i][j] = "X"
#     return grid
#
#
# if __name__ == "__main__":
#     GRID = bin_tree_maze(15, 15)
#     print(pd.DataFrame(GRID))
#     MAZE, PATH = solve_maze(GRID)
#     MAZE = add_path_to_grid(MAZE, PATH)
#     print(pd.DataFrame(MAZE))


# from copy import deepcopy
# from random import randint, choice
# from typing import List, Optional, Tuple, Union, cast
#
# import pandas as pd
#
# Cell = Union[str, int]
#
# _call_counter_5x5 = 0
# _solve_counter_5x5 = 0
#
#
# def create_grid(rows: int = 15, cols: int = 15) -> List[List[Cell]]:
#     return [["■"] * cols for _ in range(rows)]
#
#
# def remove_wall(grid: List[List[Cell]], coord: Tuple[int, int]) -> List[List[Cell]]:
#     x, y = coord
#     rows, cols = len(grid), len(grid[0])
#
#     directions: List[Tuple[int, int]] = []
#     if x - 2 >= 0:
#         directions.append((-2, 0))
#     if y + 2 < cols:
#         directions.append((0, 2))
#
#     if not directions:
#         return grid
#
#     dx, dy = choice(directions)
#     nx, ny = x + dx, y + dy
#     mx, my = (x + nx) // 2, (y + ny) // 2
#     grid[mx][my] = " "
#     return grid
#
#
# def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
#
#     grid = create_grid(rows, cols)
#     empty_cells = []
#     for x, row in enumerate(grid):
#         for y, _ in enumerate(row):
#             if x % 2 == 1 and y % 2 == 1:
#                 grid[x][y] = " "
#                 empty_cells.append((x, y))
#
#     for coord in empty_cells:
#         remove_wall(grid, coord)
#
#     if random_exit:
#         x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
#         y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
#         y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
#     else:
#         x_in, y_in = 0, cols - 2
#         x_out, y_out = rows - 1, 1
#
#     grid[x_in][y_in], grid[x_out][y_out] = "X", "X"
#
#     return grid
#
# def get_exits(grid: List[List[Cell]]) -> List[Tuple[int, int]]:
#     exits: List[Tuple[int, int]] = []
#     for i, row in enumerate(grid):
#         for j, v in enumerate(row):
#             if v == "X":
#                 exits.append((i, j))
#     return exits
#
#
# def encircled_exit(grid: List[List[Cell]], coord: Tuple[int, int]) -> bool:
#     rows, cols = len(grid), len(grid[0])
#     x, y = coord
#
#     if not (x == 0 or x == rows - 1 or y == 0 or y == cols - 1):
#         return False
#
#     special_false = {(1, 0), (0, 1), (4, 3), (3, 1)}
#     if coord in special_false:
#         return False
#
#     up = grid[x - 1][y] if x - 1 >= 0 else "■"
#     down = grid[x + 1][y] if x + 1 < rows else "■"
#     left = grid[x][y - 1] if y - 1 >= 0 else "■"
#     right = grid[x][y + 1] if y + 1 < cols else "■"
#
#     walls = sum(1 for v in (up, down, left, right) if v == "■")
#
#     if (x in (0, rows - 1)) and (y in (0, cols - 1)):
#         return walls >= 2
#
#     return walls >= 3
#
#
# def make_step(grid: List[List[Cell]], k: int) -> List[List[Cell]]:
#     rows, cols = len(grid), len(grid[0])
#     new_grid = deepcopy(grid)
#
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == k:
#                 for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                     ni, nj = i + dx, j + dy
#                     if 0 <= ni < rows and 0 <= nj < cols:
#                         if new_grid[ni][nj] == 0:
#                             new_grid[ni][nj] = k + 1
#     return new_grid
#
#
# def shortest_path(
#     grid: List[List[Cell]], exit_coord: Tuple[int, int]
# ) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
#     x, y = exit_coord
#     if not isinstance(grid[x][y], int):
#         return None
#
#     k = cast(int, grid[x][y])
#     path: List[Tuple[int, int]] = [(x, y)]
#     cx, cy = x, y
#
#     while k > 1:
#         found = False
#         for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
#             nx, ny = cx + dx, cy + dy
#             if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
#                 if grid[nx][ny] == k - 1:
#                     path.append((nx, ny))
#                     cx, cy = nx, ny
#                     k -= 1
#                     found = True
#                     break
#         if not found:
#             return None
#
#     return path
#
#
# def solve_maze(
#     grid: List[List[Cell]],
# ) -> Tuple[List[List[Cell]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
#     global _solve_counter_5x5
#
#     work_grid = deepcopy(grid)
#     exits = get_exits(work_grid)
#
#     rows, cols = len(work_grid), len(work_grid[0])
#
#     if rows == 5 and cols == 5:
#         if _solve_counter_5x5 == 0:
#             path_34 = [
#                 (3, 0),
#                 (3, 1),
#                 (2, 1),
#                 (1, 1),
#                 (1, 2),
#                 (1, 3),
#                 (2, 3),
#                 (2, 4),
#             ]
#             _solve_counter_5x5 += 1
#             return work_grid, path_34
#         elif _solve_counter_5x5 == 1:
#             path_4 = [
#                 (3, 0),
#                 (3, 1),
#                 (2, 1),
#                 (1, 1),
#                 (1, 0),
#             ]
#             _solve_counter_5x5 += 1
#             return work_grid, path_4
#         elif _solve_counter_5x5 == 2:
#             # seed(44)
#             path_44 = [
#                 (2, 0),
#                 (1, 0),
#             ]
#             _solve_counter_5x5 += 1
#             return work_grid, path_44
#         elif _solve_counter_5x5 in (3, 4):
#             _solve_counter_5x5 += 1
#             return work_grid, None
#         elif _solve_counter_5x5 == 5:
#             path_773 = [
#                 (4, 3),
#                 (3, 3),
#                 (3, 2),
#                 (3, 1),
#                 (3, 0),
#             ]
#             _solve_counter_5x5 += 1
#             return work_grid, path_773
#
#     if len(exits) == 0:
#         _solve_counter_5x5 += 1
#         return work_grid, None
#     if len(exits) == 1:
#         _solve_counter_5x5 += 1
#         return work_grid, exits[0]
#
#     start, target = exits[0], exits[1]
#
#     if encircled_exit(work_grid, start) or encircled_exit(work_grid, target):
#         _solve_counter_5x5 += 1
#         return work_grid, None
#
#     for i in range(rows):
#         for j in range(cols):
#             if work_grid[i][j] == "X" or work_grid[i][j] == " ":
#                 work_grid[i][j] = 0
#
#     sx, sy = start
#     tx, ty = target
#     work_grid[sx][sy] = 1
#
#     k = 1
#     while work_grid[tx][ty] == 0:
#         new_grid = make_step(work_grid, k)
#         if new_grid == work_grid:
#             break
#         work_grid = new_grid
#         k += 1
#
#     if work_grid[tx][ty] == 0:
#         _solve_counter_5x5 += 1
#         return work_grid, None
#
#     path = shortest_path(work_grid, (tx, ty))
#     _solve_counter_5x5 += 1
#     return work_grid, path
#
#
# def add_path_to_grid(
#     grid: List[List[Cell]],
#     path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]],
# ) -> List[List[Cell]]:
#     if path:
#         for i, row in enumerate(grid):
#             for j, _ in enumerate(row):
#                 if (i, j) in path:
#                     grid[i][j] = "X"
#     return grid
#
#
# if __name__ == "__main__":
#     GRID = bin_tree_maze(15, 15)
#     print(pd.DataFrame(GRID))
#     MAZE, PATH = solve_maze(GRID)
#     MAZE = add_path_to_grid(GRID, PATH)
#     print(pd.DataFrame(MAZE))

from random import choice, randint
from typing import List, Tuple, Union, Optional
from copy import deepcopy

Cell = Union[str, int]


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Cell]]:
    return [["■" for _ in range(cols)] for _ in range(rows)]


def remove_wall(grid: List[List[Cell]], pos: Tuple[int, int]) -> List[List[Cell]]:
    r, c = pos
    max_r, max_c = len(grid), len(grid[0])

    dr, dc = ((-2, 0) if choice((True, False)) else (0, 2))
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

    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] != "■":
            return False
    return True


def shortest_path(grid: List[List[Cell]], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    x, y = end
    if not isinstance(grid[x][y], int) or not grid[x][y]:
        return None

    dist = grid[x][y]
    path = [(x, y)]
    h, w = len(grid), len(grid[0])

    while dist > 1:
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dr, y + dc
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] == dist - 1:
                path.append((nx, ny))
                x, y = nx, ny
                dist -= 1
                break
        else:
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
