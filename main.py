from tkinter import *
from tkinter import ttk
from tictactoe import TicTacToe

buttons = []
board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']
         ]
game = TicTacToe(board)
root = Tk()
root.title("Tic Tac Toe")
root.geometry("500x500")
root.configure(bg="#2b2d42")

BG_COLOR = "#2b2d42"
FRAME_COLOR = "#2b2d42"
BTN_COLOR = "#8d99ae"
BTN_HOVER = "#edf2f4"
X_COLOR = "#ef233c"
O_COLOR = "#2196f3"
TEXT_COLOR = "#edf2f4"

FONT_TITLE = ("Helvetica", 20, "bold")
FONT_BTN = ("Helvetica", 14, "bold")
FONT_CELL = ("Helvetica", 32, "bold")
FONT_RESULT = ("Helvetica", 22, "bold")

# ttk widgets render bg/fg reliably across platforms (macOS Aqua theme
# ignores color options on classic tk.Button until the widget is
# interacted with), so we switch buttons to ttk with a custom "clam" style.
style = ttk.Style(root)
style.theme_use("clam")

style.configure("TButton", background=BTN_COLOR, foreground=TEXT_COLOR,
                 font=FONT_BTN, borderwidth=0, focusthickness=0, relief="flat")
style.map("TButton",
          background=[("active", BTN_HOVER), ("pressed", BTN_HOVER)],
          foreground=[("active", BG_COLOR), ("pressed", BG_COLOR)])

style.configure("Menu.TButton", font=FONT_BTN, padding=10)

style.configure("Cell.TButton", font=FONT_CELL)
style.configure("X.TButton", font=FONT_CELL, foreground=X_COLOR)
style.map("X.TButton",
          background=[("active", BTN_HOVER), ("pressed", BTN_HOVER)],
          foreground=[("active", X_COLOR), ("pressed", X_COLOR)])
style.configure("O.TButton", font=FONT_CELL, foreground=O_COLOR)
style.map("O.TButton",
          background=[("active", BTN_HOVER), ("pressed", BTN_HOVER)],
          foreground=[("active", O_COLOR), ("pressed", O_COLOR)])

menu_frame = Frame(root, height=600, width=600, relief=SUNKEN, bg=FRAME_COLOR)
game_frame = Frame(root, relief=SUNKEN, bg=FRAME_COLOR)
result_frame = Frame(root, relief='raised', borderwidth=5, bg=FRAME_COLOR)
choose_frame = Frame(root, relief=SUNKEN, bg=FRAME_COLOR)


def color_cell(btn, value):
    if value == "X":
        btn.configure(style="X.TButton")
    elif value == "O":
        btn.configure(style="O.TButton")


def reset_game():
    global board, buttons, game
    for widget in game_frame.winfo_children():
        widget.destroy()
    for widget in result_frame.winfo_children():
        widget.destroy()
    for widget in choose_frame.winfo_children():
        widget.destroy()
    result_frame.pack_forget()
    choose_frame.pack_forget()
    buttons = []
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]
    game = TicTacToe(board)


def show_result():
    game_frame.pack_forget()
    result_frame.pack(expand=True, fill=BOTH)
    terminal = game.isTerminal(board)
    if terminal == "TIE!":
        text = f'game over \n {terminal}'
    else:
        text = f'game over \n {terminal} won '
    label = Label(result_frame, text=text, width=30, height=15,
                  bg=FRAME_COLOR, fg=TEXT_COLOR, font=FONT_RESULT)
    label.pack()


def on_click_multi(i: int, j: int):
    if board[i][j] != "_":
        return
    if game.player(board) == "X's turn":
        board[i][j] = "X"
        buttons[i][j].config(text=board[i][j])
        color_cell(buttons[i][j], board[i][j])
    else:
        board[i][j] = "O"
        buttons[i][j].config(text=board[i][j])
        color_cell(buttons[i][j], board[i][j])

    if game.isTerminal(board):
        show_result()


def on_click_singl(i: int, j: int):
    if board[i][j] != "_":
        return

    if human_char == "X":
        if game.player(board) != "X's turn":
            return
        board[i][j] = "X"
        buttons[i][j].config(text=board[i][j])
        color_cell(buttons[i][j], board[i][j])
        if game.isTerminal(board):
            show_result()
            return
        ai_row, ai_col = game.best_move(board, max_player=False)
        if ai_row is not None:
            board[ai_row][ai_col] = "O"
            buttons[ai_row][ai_col].config(text="O")
            color_cell(buttons[ai_row][ai_col], "O")
    else:
        if game.player(board) != "O's turn":
            return
        board[i][j] = "O"
        buttons[i][j].config(text=board[i][j])
        color_cell(buttons[i][j], board[i][j])
        if game.isTerminal(board):
            show_result()
            return
        ai_row, ai_col = game.best_move(board, max_player=True)
        if ai_row is not None:
            board[ai_row][ai_col] = "X"
            buttons[ai_row][ai_col].config(text="X")
            color_cell(buttons[ai_row][ai_col], "X")

    if game.isTerminal(board):
        show_result()



def choose_char():
    reset_game()
    menu_frame.pack_forget()
    choose_frame.pack(expand=True, fill=BOTH)
    choice_label = Label(choose_frame, text="choose your character", width=20, height=5,
                          bg=FRAME_COLOR, fg=TEXT_COLOR, font=FONT_TITLE)
    choice_label.pack()
    x_button = ttk.Button(choose_frame, text="X", command=lambda: open_singl("X"),
                           width=10, style="Menu.TButton")
    x_button.pack(pady=5)
    o_button = ttk.Button(choose_frame, text="O", command=lambda: open_singl("O"),
                           width=10, style="Menu.TButton")
    o_button.pack(pady=5)


def open_singl(char):
    global human_char
    human_char = char
    choose_frame.pack_forget()
    game_frame.pack(expand=True, fill=BOTH)
    for i in range(len(board)):
        buttons.append([])
        game_frame.columnconfigure(i, weight=1, minsize=75)
        game_frame.rowconfigure(i, weight=1, minsize=50)
        for j in range(len(board[i])):
            button1 = ttk.Button(game_frame, text=board[i][j], command=lambda i=i, j=j: on_click_singl(i, j),
                                  style="Cell.TButton")
            button1.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
            buttons[i].append(button1)
    if char == "O":
        ai_row, ai_col = game.best_move(board, max_player=True)
        if ai_row is not None:
            board[ai_row][ai_col] = "X"
            buttons[ai_row][ai_col].config(text=board[ai_row][ai_col])
            color_cell(buttons[ai_row][ai_col], board[ai_row][ai_col])


def open_multi():
    reset_game()
    menu_frame.pack_forget()
    game_frame.pack(expand=True, fill=BOTH)
    for i in range(len(board)):
        buttons.append([])
        game_frame.columnconfigure(i, weight=1, minsize=75)
        game_frame.rowconfigure(i, weight=1, minsize=50)
        for j in range(len(board[i])):
            button1 = ttk.Button(game_frame, text=board[i][j], command=lambda i=i, j=j: on_click_multi(i, j),
                                  style="Cell.TButton")
            button1.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")
            buttons[i].append(button1)


title_label = Label(menu_frame, text="Tic Tac Toe", font=FONT_TITLE, bg=FRAME_COLOR, fg=TEXT_COLOR)
title_label.pack(pady=(10, 20))

btn_single = ttk.Button(menu_frame, text="singleplayer", command=choose_char,
                         width=20, style="Menu.TButton")
btn_single.pack(pady=8)

btn_multi = ttk.Button(menu_frame, text="multiplayer", command=open_multi,
                        width=20, style="Menu.TButton")
btn_multi.pack(pady=8)

menu_frame.pack(expand=True, fill=BOTH)
root.mainloop()
