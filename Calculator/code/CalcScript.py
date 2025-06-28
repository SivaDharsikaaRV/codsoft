import tkinter as tk

def button_click(char):
    entry.insert(tk.END, str(char))

def clear():
    entry.delete(0, tk.END)

def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("3D Visual Calculator")


entry = tk.Entry(root, width=25, font=('Arial', 24), bd=5, relief=tk.FLAT, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ['C', '←', '(', ')'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]


funcs = {
    'C': clear,
    '←': delete,
    '=': calculate
}


symbols = {'C', '←', '(', ')', '/', '*', '-', '+', '='}


symbol_font = ('Arial', 18, 'bold italic')
number_font = ('Arial', 18, 'bold')


for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        action = funcs.get(char, lambda ch=char: button_click(ch))

        if char in symbols:
            bg_color = 'black'
            fg_color = 'yellow'
            bd_color = 'yellow'
            font = symbol_font
        else:
            bg_color = '#ffff99'  
            fg_color = 'black'
            bd_color = 'black'
            font = number_font

        tk.Button(
            root,
            text=char,
            width=6,
            height=2,
            font=font,  
            bg=bg_color,
            fg=fg_color,
            relief='raised',
            bd=5,
            highlightbackground=bd_color,
            highlightthickness=2,
            command=action
        ).grid(row=i+1, column=j, padx=4, pady=4)

root.mainloop()
