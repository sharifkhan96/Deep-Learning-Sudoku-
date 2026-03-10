# Sudoku GUI Game (Python + Tkinter)

A desktop **Sudoku Game built with Python using Tkinter and Object-Oriented Programming (OOP)**.  
The application provides a graphical interface where users can play Sudoku, check their answers, reset the puzzle, or automatically solve the board.

This project demonstrates **Python GUI development, recursion, backtracking algorithms, and OOP design**.

---

## Features

- 9×9 interactive Sudoku board
- Built using **Tkinter GUI**
- Object-Oriented Python structure
- Sudoku **solver using backtracking**
- Input validation
- Check if your solution is correct
- Reset the puzzle
- Auto-solve feature

---

## Preview

Example Sudoku Interface:

```
+-------+-------+-------+
| 5 3 . | . 7 . | . . . |
| 6 . . | 1 9 5 | . . . |
| . 9 8 | . . . | . 6 . |
+-------+-------+-------+
| 8 . . | . 6 . | . . 3 |
| 4 . . | 8 . 3 | . . 1 |
| 7 . . | . 2 . | . . 6 |
+-------+-------+-------+
| . 6 . | . . . | 2 8 . |
| . . . | 4 1 9 | . . 5 |
| . . . | . 8 . | . 7 9 |
+-------+-------+-------+
```

Users can fill missing numbers and solve the puzzle interactively.

---

## Project Structure

```
sudoku-gui-game/
│
├── sudoku_gui.py
├── README.md
└── requirements.txt
```

Main components:

- **SudokuGame class**
- GUI grid creation
- Input validation
- Sudoku solving algorithm
- Board checking logic

---

## Technologies Used

- Python
- Tkinter
- Object-Oriented Programming (OOP)
- Backtracking Algorithm
- Recursion

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/sudoku-gui-python.git
```

Move into the project folder:

```bash
cd sudoku-gui-python
```

Run the program:

```bash
python sudoku_gui.py
```

No external libraries are required because **Tkinter comes with Python**.

---

## How the Solver Works

The Sudoku solver uses a **Backtracking Algorithm**.

Steps:

1. Find an empty cell
2. Try numbers from **1–9**
3. Check if the number is valid:
   - not in the same row
   - not in the same column
   - not in the same 3×3 box
4. Recursively solve the board
5. If a conflict occurs, backtrack and try another number

This guarantees a valid Sudoku solution if one exists.

---

## Example Algorithm

```python
def solve(board):
    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False
```

---

## Future Improvements

Possible enhancements:

- Sudoku puzzle generator
- Difficulty levels (Easy / Medium / Hard)
- Timer
- Hint system
- Keyboard navigation
- Better GUI styling
- Highlight incorrect numbers
- Dark mode UI

---

## Learning Objectives

This project helps practice:

- Python GUI development
- Object-Oriented Programming
- Algorithm design
- Backtracking techniques
- Game logic implementation

---

## License

This project is open-source and available under the **MIT License**.
