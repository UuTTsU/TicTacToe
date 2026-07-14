import copy
import os

from flask import Flask, jsonify, render_template, request, session

from tictactoe import TicTacToe

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "tictactoe-dev-secret")


def empty_board():
    return [["_", "_", "_"] for _ in range(3)]


def get_game():
    board = session.get("board", empty_board())
    mode = session.get("mode", "menu")
    human_char = session.get("human_char", "X")
    return TicTacToe(copy.deepcopy(board)), board, mode, human_char


def save_state(board, mode, human_char):
    session["board"] = board
    session["mode"] = mode
    session["human_char"] = human_char


def terminal_result(game, board):
    result = game.isTerminal(board)
    if not result:
        return None
    if result == "TIE!":
        return {"status": "tie", "message": "TIE!"}
    return {"status": "win", "message": f"{result} won"}


def ai_move(game, board, human_char):
    if human_char == "X":
        row, col = game.best_move(board, max_player=False)
        if row is not None:
            board[row][col] = "O"
    else:
        row, col = game.best_move(board, max_player=True)
        if row is not None:
            board[row][col] = "X"
    return board


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/state")
def api_state():
    game, board, mode, human_char = get_game()
    turn = game.player(board) if not game.isTerminal(board) else None
    return jsonify({
        "board": board,
        "mode": mode,
        "human_char": human_char,
        "turn": turn,
        "result": terminal_result(game, board),
    })


@app.route("/api/new", methods=["POST"])
def api_new():
    data = request.get_json(silent=True) or {}
    mode = data.get("mode", "multi")
    human_char = data.get("human_char", "X")
    board = empty_board()
    game = TicTacToe(board)

    if mode == "single" and human_char == "O":
        board = ai_move(game, board, human_char)

    save_state(board, mode, human_char)
    return jsonify({
        "board": board,
        "mode": mode,
        "human_char": human_char,
        "turn": game.player(board) if not game.isTerminal(board) else None,
        "result": terminal_result(game, board),
    })


@app.route("/api/move", methods=["POST"])
def api_move():
    data = request.get_json(silent=True) or {}
    row = data.get("row")
    col = data.get("col")

    if row is None or col is None:
        return jsonify({"error": "row and col required"}), 400

    game, board, mode, human_char = get_game()

    if game.isTerminal(board):
        return jsonify({"error": "game is over"}), 400
    if board[row][col] != "_":
        return jsonify({"error": "cell already taken"}), 400

    current_turn = game.player(board)
    if mode == "single":
        expected = f"{human_char}'s turn"
        if current_turn != expected:
            return jsonify({"error": "not your turn"}), 400
        board[row][col] = human_char
        if not game.isTerminal(board):
            board = ai_move(game, board, human_char)
    else:
        piece = "X" if current_turn == "X's turn" else "O"
        board[row][col] = piece

    save_state(board, mode, human_char)
    return jsonify({
        "board": board,
        "mode": mode,
        "human_char": human_char,
        "turn": game.player(board) if not game.isTerminal(board) else None,
        "result": terminal_result(game, board),
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=os.environ.get("FLASK_DEBUG") == "1")
