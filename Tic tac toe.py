import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
score = {"X": 0, "O": 0}


def button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            score[winner] += 1
            update_score()
            reset_board()
        elif is_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

def check_winner():
  
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
   
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_tie():
    for row in board:
        if "" in row:
            return False
    return True

def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

def update_score():
    score_label.config(text=f"Score - X: {score['X']}  O: {score['O']}")


root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 36), width=5, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

score_label = tk.Label(root, text="Score - X: 0  O: 0", font=("Arial", 14))
score_label.grid(row=3, column=0, columnspan=3, pady=10)

reset_button = tk.Button(root, text="Restart Game", font=("Arial", 14), command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3, pady=5)


root.mainloop()
