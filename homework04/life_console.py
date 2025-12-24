import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        rows, cols = self.life.rows, self.life.cols
        max_y, max_x = screen.getmaxyx()

        height = min(rows + 2, max_y)
        width = min(cols + 2, max_x)

        for x in range(width):
            screen.addch(0, x, "#")
            screen.addch(height - 1, x, "#")

        for y in range(1, height - 1):
            screen.addch(y, 0, "#")
            screen.addch(y, width - 1, "#")

    def draw_grid(self, screen) -> None:
        max_y, max_x = screen.getmaxyx()
        for r in range(min(self.life.rows, max_y - 2)):
            for c in range(min(self.life.cols, max_x - 2)):
                ch = "O" if self.life.curr_generation[r][c] == 1 else " "
                screen.addch(r + 1, c + 1, ch)

    def run(self) -> None:
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.nodelay(True)  # не блокировать getch

        try:
            while self.life.is_changing and not self.life.is_max_generations_exceeded:
                ch = screen.getch()
                # доп. задание: выход по 'q'
                if ch == ord("q"):
                    break

                screen.clear()
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.refresh()

                self.life.step()
                curses.napms(100)  # пауза 100 мс между шагами
        finally:
            curses.nocbreak()
            curses.echo()
            curses.endwin()

if __name__ == "__main__":
    import random
    random.seed(4321)
    life = GameOfLife((20, 60), randomize=True, max_generations=50)
    ui = Console(life)
    ui.run()
