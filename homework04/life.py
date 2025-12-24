import pathlib
import random
import typing as tp

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True, max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        self.rows, self.cols = size
        self.prev_generation = self.create_grid()
        self.curr_generation = self.create_grid(randomize=randomize)
        self.max_generations = max_generations
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        """Создание матрицы клеток rows x cols."""
        grid: Grid = []
        for _ in range(self.rows):
            row: Cells = []
            for _ in range(self.cols):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        """Вернуть значения соседних клеток для клетки cell."""
        row, col = cell
        neighbours: Cells = []
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy == 0 and dx == 0:
                    continue
                nr, nc = row + dy, col + dx
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbours.append(self.curr_generation[nr][nc])
        return neighbours

    def get_next_generation(self) -> Grid:
        """Получить следующее поколение клеток."""
        new_grid: Grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                alive = self.curr_generation[r][c] == 1
                neighbours = self.get_neighbours((r, c))
                alive_count = sum(neighbours)

                if alive and alive_count in (2, 3):
                    new_grid[r][c] = 1
                elif not alive and alive_count == 3:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = 0
        return new_grid

    def step(self) -> None:
        """Выполнить один шаг игры."""
        self.prev_generation = [row[:] for row in self.curr_generation]
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """Не превысило ли текущее число поколений максимально допустимое."""
        return self.generations >= self.max_generations

    @property
    def is_changing(self) -> bool:
        """Изменилось ли состояние клеток с предыдущего шага."""
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """Прочитать состояние клеток из указанного файла."""
        text = filename.read_text().strip().splitlines()
        grid: Grid = []
        for line in text:
            row = [1 if ch == "1" else 0 for ch in line.strip()]
            grid.append(row)

        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        life = GameOfLife((rows, cols), randomize=False)
        life.curr_generation = grid
        life.prev_generation = life.create_grid()
        life.generations = 1
        return life

    def save(self, filename: pathlib.Path) -> None:
        """Сохранить текущее состояние клеток в указанный файл."""
        lines = []
        for row in self.curr_generation:
            line = "".join("1" if cell == 1 else "0" for cell in row)
            lines.append(line)
        filename.write_text("\n".join(lines))
