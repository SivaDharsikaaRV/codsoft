import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    chars = ''
    if uppercase_var.get(): chars += string.ascii_uppercase
    if lowercase_var.get(): chars += string.ascii_lowercase
    if numbers_var.get(): chars += string.digits
    if symbols_var.get(): chars += string.punctuation
    if chars:
        length = min(max(length_var.get(), 5), 15)
        password = ''.join(random.choice(chars) for _ in range(length))
        password_var.set(password)

root = tk.Tk()
root.geometry('800x600')
root.title('Password Generator')
root.config(bg='black')  # Set black background

length_var = tk.IntVar(value=12)
password_var = tk.StringVar()
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

# Title Label
tk.Label(root, text='Password Generator', fg='white', bg='black', font=('Arial', 32, 'bold')).pack(pady=20)

# Password Length Label and Slider
tk.Label(root, text='Password Length', fg='white', bg='black', font=('Arial', 24, 'bold')).pack()
slider = ttk.Scale(root, from_=5, to=15, variable=length_var, orient='horizontal', length=500)
slider.pack(pady=15)

# Checkbuttons for options
cb_frame = tk.Frame(root, bg='black')
cb_frame.pack(pady=10, anchor='w', padx=60)

tk.Checkbutton(cb_frame, text='Include Uppercase', variable=uppercase_var, fg='white', bg='black', selectcolor='black', font=('Arial', 22, 'bold')).pack(anchor='w')
tk.Checkbutton(cb_frame, text='Include Lowercase', variable=lowercase_var, fg='white', bg='black', selectcolor='black', font=('Arial', 22, 'bold')).pack(anchor='w')
tk.Checkbutton(cb_frame, text='Include Numbers', variable=numbers_var, fg='white', bg='black', selectcolor='black', font=('Arial', 22, 'bold')).pack(anchor='w')
tk.Checkbutton(cb_frame, text='Include Symbols', variable=symbols_var, fg='white', bg='black', selectcolor='black', font=('Arial', 22, 'bold')).pack(anchor='w')

# Generate button
tk.Button(root, text='Generate Password', command=generate_password, bg='white', fg='black', font=('Arial', 22, 'bold')).pack(pady=25)

# Password entry box
password_entry = tk.Entry(root, textvariable=password_var, width=60, font=('Arial', 20), relief='solid', bd=2, bg='black', fg='white', insertbackground='white')
password_entry.pack(pady=15)
password_entry.config(highlightbackground="white", highlightcolor="white", highlightthickness=2, relief='groove')

root.mainloop()
