"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
#X_TURN = True

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    
    # if board == initial_state():
    #     return X
    # elif X_TURN:
    #     X_TURN = False
    #     return O
    # return X

    num_x = 0
    num_o = 0
    for r in board:
        for c in r:
            if c == "X":
                num_x += 1
            elif c == "O":
                num_o += 1
    
    if num_x - num_o == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    
    possible = set()
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                possible.add((r,c))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None or action == set(): return board
    r,c = action[0], action[1]
    if board[r][c] != EMPTY: raise ValueError
    copy_board = copy.deepcopy(board)
    copy_board[r][c] = player(board)
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Testing horizontals
    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] != EMPTY:
            return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] != EMPTY:
            return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] != EMPTY:
            return board[2][0]
    # Testing Verticals
    elif board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] != EMPTY:
            return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] != EMPTY:
            return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] != EMPTY:
            return board[0][2]
    # Testing Diagonals
    elif board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != EMPTY:
            return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != EMPTY:
            return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for r in board:
        for c in r:
            if c == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None

    moves = actions(board)
    move_values = []

    for m in moves:
        new_board = result(board, m)
        if player(new_board) == X:
            move_values.append((m, max_func(new_board)))
        else:
            move_values.append((m, min_func(new_board)))
    
    optimal_move = move_values[0]
    if player(board) == X:
        for v in move_values:
            if v[1] > optimal_move[1]:
                optimal_move = v
    else:
        for v in move_values:
            if v[1] < optimal_move[1]:
                optimal_move = v
    
    return optimal_move[0]


def max_func(state):
    if terminal(state):
        return utility(state)
    
    v = float('-inf')

    for a in actions(state):
        v = max(v, min_func(result(state, a)))
    
    return v

def min_func(state):
    if terminal(state):
        return utility(state)

    v = float('inf')

    for a in actions(state):
        v = min(v, max_func(result(state, a)))
    
    return v