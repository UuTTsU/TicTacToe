# Tic Tac Toe

A desktop Tic Tac Toe game built with Python's `tkinter`, featuring a minimax-powered AI opponent for single-player mode and a local pass-and-play multiplayer mode.

## Features

- **Single-player mode** — play against an unbeatable AI powered by the minimax algorithm. Choose to play as X (go first) or O (go second).
- **Multiplayer mode** — two players take turns on the same device.
- **Responsive UI** — styled with `ttk` and a custom `clam` theme for consistent, cross-platform rendering (colors and fonts display correctly on macOS, Windows, and Linux).
- **Color-coded moves** — X and O are rendered in distinct colors for readability.
- **Win/tie detection** — checks rows, columns, and diagonals after every move, and reports the result on a dedicated end screen.

## Project structure

```
TicTacToe/
├── main.py         # tkinter GUI: menus, game board, event handling
├── tictactoe.py     # Game logic: rules, state, and the minimax AI
└── README.md
```

### `tictactoe.py`

Contains the `TicTacToe` class, which is independent of the GUI and handles all game rules:

- `player(board)` — determines whose turn it is
- `action(board)` — lists available (empty) cells
- `result(board, action)` — returns the board state after a move
- `isTerminal(board)` — checks for a win, loss, or tie
- `utility(board)` — scores a terminal board state (`1` = X wins, `-1` = O wins, `0` = tie)
- `minimax(board, max_player)` — recursively evaluates the game tree
- `best_move(board, max_player)` — returns the optimal `(row, col)` move for the given player

### `main.py`

Builds the GUI with `tkinter`/`ttk`:

- **Menu screen** — choose single-player or multiplayer
- **Character select screen** (single-player only) — choose to play as X or O
- **Game board screen** — a 3x3 grid of buttons; clicking an empty cell places a move
- **Result screen** — shown when the game ends, displaying the winner or a tie

## Requirements

- Python 3.8+
- `tkinter` (included with most standard Python installations; on some Linux distributions it must be installed separately, e.g. `sudo apt install python3-tk`)

No external dependencies are required.

## Running the game

```bash
python3 main.py
```

## How to play

1. Launch the app and choose **singleplayer** or **multiplayer** from the main menu.
2. In single-player mode, pick whether you want to play as **X** or **O**. X always moves first — if you choose O, the AI takes the opening move automatically.
3. Click any empty cell on the board to place your mark.
4. The game ends automatically when there's a win (row, column, or diagonal) or the board fills up with no winner (tie), and the result is shown on the end screen.

## Notes

- The AI in single-player mode plays optimally (via minimax with no depth limit), so it cannot be beaten — the best achievable outcome against it is a tie.
- The GUI uses the `ttk` "clam" theme rather than raw `tk.Button` styling, since some platforms (notably macOS's native Aqua theme) don't reliably render custom button colors otherwise.
