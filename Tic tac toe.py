from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")

player = "X"

board = [["" for _ in range(3)] for _ in range(3)]


def handle_click(i, j):
    global player
    if buttons[i][j]["text"] == "":
        buttons[i][j]["text"] = player
        board[i][j] = player

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif all(board[row][col] != "" for row in range(3) for col in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"

def check_winner():
    
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def reset_game():
    global board, player
    board = [["" for _ in range(3)] for _ in range(3)]
    player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        btn = Button(root, text="", font=("Arial", 24), width=5, height=2,
                     command=lambda i=i, j=j: handle_click(i, j))
        btn.grid(row=i, column=j)
        buttons[i][j] = btn

root.mainloop()

reset_button = tk.Button(root, text="Restart Game", font=("Arial", 14), command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3, pady=5)


root.mainloop()
