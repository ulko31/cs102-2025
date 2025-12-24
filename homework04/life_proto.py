import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.speed = speed

        self.grid: Grid = self.create_grid(randomize=False)

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        if not hasattr(self, "grid"):
            self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.grid = self.get_next_generation()

            self.screen.fill(pygame.Color("white"))
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.
        """
        grid: Grid = []
        for _ in range(self.cell_height):
            row: Cells = []
            for _ in range(self.cell_width):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for y in range(self.cell_height):
            for x in range(self.cell_width):
                color = pygame.Color("green") if self.grid[y][x] == 1 else pygame.Color("white")
                rect = pygame.Rect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, color, rect)

    def get_neighbours(self, cell: Cell) -> Cells:
        row, col = cell
        neighbours: Cells = []

        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dy == 0 and dx == 0:
                    continue
                nr, nc = row + dy, col + dx
                if 0 <= nr < self.cell_height and 0 <= nc < self.cell_width:
                    neighbours.append(self.grid[nr][nc])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid: Grid = [
            [0 for _ in range(self.cell_width)] for _ in range(self.cell_height)
        ]

        for r in range(self.cell_height):
            for c in range(self.cell_width):
                alive = self.grid[r][c] == 1
                neighbours = self.get_neighbours((r, c))
                alive_count = sum(neighbours)

                if alive and alive_count in (2, 3):
                    new_grid[r][c] = 1
                elif not alive and alive_count == 3:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = 0

        return new_grid


if __name__ == "__main__":
    game = GameOfLife(width=320, height=240, cell_size=20, speed=10)
    game.grid = game.create_grid(randomize=True)
    game.run()
