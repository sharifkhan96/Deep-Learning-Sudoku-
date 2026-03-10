import tkinter as tk
from tkinter import messagebox
import copy


class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Game - Tkinter OOP")
        self.root.resizable(False, False)

        self.original_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],

            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],

            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        self.board = copy.deepcopy(self.original_board)
        self.cells = []

        self.create_title()
        self.create_grid()
        self.create_buttons()
        self.load_board()

    def create_title(self):
        title = tk.Label(
            self.root,
            text="Sudoku Game",
            font=("Arial", 18, "bold"),
            pady=10
        )
        title.grid(row=0, column=0, columnspan=9)

    def create_grid(self):
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.grid(row=1, column=0, columnspan=9)

        for row in range(9):
            row_cells = []
            for col in range(9):
                entry = tk.Entry(
                    frame,
                    width=2,
                    font=("Arial", 20),
                    justify="center",
                    bd=2,
                    relief="solid"
                )

                padx = (2, 2)
                pady = (2, 2)

                if col in [2, 5]:
                    padx = (2, 6)
                if row in [2, 5]:
                    pady = (2, 6)

                entry.grid(row=row, column=col, padx=padx, pady=pady)
                entry.bind("<KeyRelease>", self.validate_input)
                row_cells.append(entry)

            self.cells.append(row_cells)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, pady=10)
        button_frame.grid(row=2, column=0, columnspan=9)

        check_btn = tk.Button(button_frame, text="Check", width=12, command=self.check_board)
        check_btn.grid(row=0, column=0, padx=5)

        solve_btn = tk.Button(button_frame, text="Solve", width=12, command=self.solve_board)
        solve_btn.grid(row=0, column=1, padx=5)

        reset_btn = tk.Button(button_frame, text="Reset", width=12, command=self.reset_board)
        reset_btn.grid(row=0, column=2, padx=5)

    def load_board(self):
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                value = self.board[row][col]

                cell.config(state="normal")
                cell.delete(0, tk.END)

                if value != 0:
                    cell.insert(0, str(value))
                    cell.config(
                        state="disabled",
                        disabledforeground="black",
                        bg="#d9d9d9"
                    )
                else:
                    cell.config(bg="white")

    def validate_input(self, event):
        widget = event.widget
        value = widget.get()

        if len(value) > 1 or (value and (not value.isdigit() or value == "0")):
            widget.delete(0, tk.END)

    def get_current_board(self):
        current = []

        for row in range(9):
            current_row = []
            for col in range(9):
                value = self.cells[row][col].get()
                if value == "":
                    current_row.append(0)
                else:
                    current_row.append(int(value))
            current.append(current_row)

        return current

    def check_board(self):
        current = self.get_current_board()

        for row in range(9):
            for col in range(9):
                num = current[row][col]

                if num == 0:
                    messagebox.showinfo("Incomplete", "The Sudoku board is not complete yet.")
                    return

                current[row][col] = 0
                if not self.is_valid(current, row, col, num):
                    current[row][col] = num
                    messagebox.showerror("Incorrect", f"Wrong value at row {row + 1}, column {col + 1}")
                    return
                current[row][col] = num

        messagebox.showinfo("Success", "Congratulations! You solved the Sudoku.")

    def reset_board(self):
        self.board = copy.deepcopy(self.original_board)
        self.load_board()

    def solve_board(self):
        current = self.get_current_board()

        if self.solve(current):
            for row in range(9):
                for col in range(9):
                    cell = self.cells[row][col]
                    if self.original_board[row][col] == 0:
                        cell.delete(0, tk.END)
                        cell.insert(0, str(current[row][col]))
            messagebox.showinfo("Solved", "Sudoku solved successfully.")
        else:
            messagebox.showerror("No Solution", "This Sudoku puzzle has no solution.")

    def is_valid(self, board, row, col, num):
        for x in range(9):
            if board[row][x] == num:
                return False

        for x in range(9):
            if board[x][col] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def find_empty(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None

    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True

        row, col = empty

        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board[row][col] = num

                if self.solve(board):
                    return True

                board[row][col] = 0

        return False


if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()