# Tic Tac Toe

A Tic Tac Toe game with singleplayer (minimax AI) and multiplayer modes — available as a **desktop app** (tkinter) and a **web app** (Flask).

## Features

- **Single-player mode** — play against an unbeatable AI powered by minimax. Choose X (go first) or O (go second).
- **Multiplayer mode** — two players take turns on the same device or browser.
- **Responsive UI** — color-coded X/O, win/tie detection, and a polished dark theme.

## Project structure

| File | Description |
|------|-------------|
| `tictactoe.py` | Game logic and minimax AI |
| `main.py` | Desktop GUI (tkinter) |
| `web_app.py` | Flask web server |
| `templates/index.html` | Web frontend |

## Desktop app

```bash
python3 main.py
```

Requires Python 3.8+ with `tkinter` (included on most systems).

## Web app (run locally)

```bash
pip install -r requirements.txt
python web_app.py
```

Open http://localhost:5000 in your browser.

> On macOS, port 5000 may be taken by AirPlay Receiver. Use `PORT=5001 python web_app.py` instead.

## Deploy globally (free on Render)

1. Push this repo to GitHub.
2. Go to [render.com](https://render.com) → **New** → **Blueprint**.
3. Connect the `UuTTsU/TicTacToe` repo — Render reads `render.yaml` automatically.
4. Click **Apply**. You get a public URL like `https://tictactoe.onrender.com`.

### Alternative: Railway

```bash
railway login
railway init
railway up
```

Start command (set automatically via `railway.toml`):
`gunicorn web_app:app --bind 0.0.0.0:$PORT`

## How to play

1. Choose **Singleplayer** or **Multiplayer**.
2. In single-player, pick **X** or **O**. X moves first — if you pick O, the AI opens.
3. Click an empty cell to place your mark.
4. The game ends on a win or tie.

## Notes

- The AI plays optimally via minimax — the best you can do is force a tie.
- The desktop GUI uses the `ttk` "clam" theme for consistent colors across macOS, Windows, and Linux.
