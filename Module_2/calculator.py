import tkinter as tk
from tkinter import PhotoImage

def on_click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button_text)

def on_clear():
    entry.delete(0, tk.END)

def on_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# main window
root = tk.Tk()
root.title("Calculate with Tuwaiger Hessah :) ")
root.configure(bg="#FFC0CB")

# Entry field
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right", bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == "=":
        cmd = on_equal
    elif text == "C":
        cmd = on_clear
    else:
        cmd = lambda t=text: on_click(t)

    tk.Button(
        root, text=text, width=5, height=2, font=("Arial", 18),
        command=cmd, bg="#FFB6C1", fg="black", activebackground="#FF69B4"
    ).grid(row=row, column=col, padx=5, pady=5)

# logo image
try:
    logo_image = PhotoImage(file="logo.png")
    logo_label = tk.Label(root, image=logo_image, bg="#FFC0CB")
    logo_label.grid(row=5, column=3, padx=5, pady=5, sticky="se")
except Exception as e:
    print("Could not load logo:", e)

root.mainloop()
