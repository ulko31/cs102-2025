import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from typing import List

from maze import add_path_to_grid, bin_tree_maze, solve_maze


def draw_cell(x_coord: int, y_coord: int, color: str, size: int = 10) -> None:
    x_pos = x_coord * size
    y_pos = y_coord * size
    x_end = x_pos + size
    y_end = y_pos + size
    canvas.create_rectangle(x_pos, y_pos, x_end, y_end, fill=color)


def draw_maze(grid: List[List[str]], size: int = 10) -> None:
    canvas.delete("all")
    for x_pos, row in enumerate(grid):
        for y_pos, cell in enumerate(row):
            if cell == " ":
                color = "white"
            elif cell == "■":
                color = "black"
            elif cell == "X":
                color = "red"
            else:
                color = "white"
            draw_cell(y_pos, x_pos, color, size)


def show_solution() -> None:
    maze_copy, path = solve_maze(GRID)
    if path:
        solved_maze = add_path_to_grid(maze_copy, path)
        draw_maze(solved_maze, CELL_SIZE)
    else:
        messagebox.showinfo("Message", "No solutions found")


def main() -> None:
    global GRID, CELL_SIZE, canvas

    rows, cols = 51, 77
    CELL_SIZE = 10
    GRID = bin_tree_maze(rows, cols)

    window = tk.Tk()
    window.title("Maze")
    window_width = cols * CELL_SIZE + 100
    window_height = rows * CELL_SIZE + 100
    window.geometry(f"{window_width}x{window_height}")

    canvas = tk.Canvas(window, width=cols * CELL_SIZE, height=rows * CELL_SIZE)
    canvas.pack()

    draw_maze(GRID, CELL_SIZE)
    solve_button = ttk.Button(window, text="Solve", command=show_solution)
    solve_button.pack(pady=20)

    window.mainloop()


if __name__ == "__main__":
    main()