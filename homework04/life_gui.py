import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        self.speed = speed

        self.width = self.life.cols * self.cell_size
        self.height = self.life.rows * self.cell_size
        self.screen_size = (self.width, self.height)

        pygame.init()
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Game of Life")

    def draw_lines(self) -> None:
        """Отрисовать сетку."""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        """Отрисовать клетки текущего поколения."""
        for r in range(self.life.rows):
            for c in range(self.life.cols):
                color = pygame.Color("green") if self.life.curr_generation[r][c] == 1 else pygame.Color("white")
                rect = pygame.Rect(
                    c * self.cell_size,
                    r * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, color, rect)

    def run(self) -> None:
        """Основной игровой цикл."""
        clock = pygame.time.Clock()
        running = True
        paused = False

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        paused = not paused
                elif event.type == MOUSEBUTTONDOWN and paused:
                    x, y = pygame.mouse.get_pos()
                    col = x // self.cell_size
                    row = y // self.cell_size
                    if 0 <= row < self.life.rows and 0 <= col < self.life.cols:
                        self.life.curr_generation[row][col] ^= 1

            if not paused and self.life.is_changing and not self.life.is_max_generations_exceeded:
                self.life.step()

            self.screen.fill(pygame.Color("white"))
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()


if __name__ == "__main__":
    import random

    random.seed(1234)
    life = GameOfLife((40, 60), randomize=True, max_generations=200)
    gui = GUI(life, cell_size=10, speed=15)
    gui.run()
