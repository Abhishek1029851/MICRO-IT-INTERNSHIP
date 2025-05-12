from tkinter import *
from tkinter import messagebox

r=Tk();r.title("Tic Tac Toe")
p="X";b=[[""for _ in range(3)]for _ in range(3)]

def c(i,j):
 global p
 if t[i][j]["text"]=="":t[i][j]["text"]=b[i][j]=p
 if any(all(b[i][x]==p for x in range(3))or all(b[x][i]==p for x in range(3))for i in range(3))or \
    all(b[x][x]==p for x in range(3))or all(b[x][2-x]==p for x in range(3)):
  messagebox.showinfo("Win",p+" wins!");res()
 elif all(b[i][j] for i in range(3)for j in range(3)):messagebox.showinfo("Draw","Tie!");res()
 else:p="O"if p=="X"else"X"

def res():
 global b,p;b=[[""for _ in range(3)]for _ in range(3)]
 for i in range(3):
  for j in range(3):t[i][j].config(text="");p="X"

t=[[Button(r,text="",font=("",24),width=4,height=2,command=lambda i=i,j=j:c(i,j))
   for j in range(3)]for i in range(3)]
for i in range(3):
 for j in range(3):t[i][j].grid(row=i,column=j)

r.mainloop()
reset_button = tk.Button(root, text="Restart Game", font=("Arial", 14), command=reset_board)
reset_button.grid(row=4, column=0, columnspan=3, pady=5)


root.mainloop()
