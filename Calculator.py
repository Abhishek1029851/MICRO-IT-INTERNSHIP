import tkinter as tk

def on_click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "←":
        entry.delete(len(entry.get())-1, tk.END)
    else:
        if entry.get() == "Error":
            entry.delete(0, tk.END)
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("300x400")
root.configure(bg="black")

entry = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=8)

buttons = [
    ['C', '←', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=']
]

for row_vals in buttons:
    row = tk.Frame(root)
    row.pack(expand=True, fill="both")
    for char in row_vals:
        btn = tk.Button(row, text=char, font=("Arial", 16), bg="#333", fg="white")
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", on_click)

root.mainloop()



