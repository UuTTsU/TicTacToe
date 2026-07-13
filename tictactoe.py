from collections import Counter
import copy


class TicTacToe:

    def __init__(self, board):
        self.board = board

    def isTerminal(self, board):
        l_diagonal = []
        r_diagonal = []

        for i in range(len(board)):
            l_diagonal.append(board[i][i])
            r_diagonal.append(board[i][(len(board) - 1) - i])

        if len(set(l_diagonal)) == 1 and l_diagonal[0] != "_":
            return l_diagonal[0]

        elif len(set(r_diagonal)) == 1 and r_diagonal[0] != "_":
            return r_diagonal[0]

        for i in range(len(board)):
            col_list = [board[j][i] for j in range(len(board[i]))]

            if len(set(board[i])) == 1 and board[i][0] != "_":
                return board[i][0]
            elif len(set(col_list)) == 1 and col_list[0] != "_":
                return col_list[0]

            else:
                continue
        lst = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                lst.append(board[i][j])
        if "_" not in lst:
            return "TIE!"
        else:
            return False

    def player(self, board):
        lst = []
        if not self.isTerminal(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] != "_":
                        lst.append(board[i][j])
                    else:
                        continue
        else:
            return "game is over"
        counter_dict = Counter(lst)
        if counter_dict["X"] > counter_dict["O"] or len(counter_dict) == 1:
            return f"O's turn"
        else:
            return "X's turn"

    def action(self, board):
        free_spaces = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "_":
                    free_spaces.append((i, j))
        return free_spaces

    def result(self, board, action):
        temp_board = copy.deepcopy(board)
        i, j = action
        if self.player(board) == "X's turn":
            temp_board[i][j] = "X"

        elif self.player(board) == "O's turn":
            temp_board[i][j] = "O"
        else:
            return "game is over"
        return temp_board

    def utility(self, board):
        if self.isTerminal(board) == "X":
            return 1
        elif self.isTerminal(board) == "O":
            return -1
        else:
            return 0

    def minimax(self, board, max_player):

        if self.isTerminal(board):
            return self.utility(board)
        if max_player:
            value = float('-inf')
            for i, j in self.action(board):
                value = max(value, self.minimax(self.result(board, (i, j)), max_player=False))

            return value
        else:
            value = float('inf')
            for i, j in self.action(board):
                value = min(value, self.minimax(self.result(board, (i, j)), max_player=True))

            return value

    def best_move(self, board, max_player):
        row, col = [0, 0]

        if self.isTerminal(board):
            return self.utility(board)
        if max_player:
            best_score = float('-inf')
            for i, j in self.action(board):
                score = self.minimax(self.result(board, (i, j)), max_player=True)
                if score > best_score:
                    best_score = score
                    row, col = i, j
            return row,col
        else:
            best_score = float('inf')
            for i, j in self.action(board):
                score = self.minimax(self.result(board, (i, j)), max_player=False)
                if score < best_score:
                    best_score = score
                    row, col = i, j
            return row, col


board = [['X', 'O', 'X'],
         ['O', 'X', '_'],
         ['_', 'O', '_']
         ]

game = TicTacToe(board)
print(game.best_move(board, max_player=True))
