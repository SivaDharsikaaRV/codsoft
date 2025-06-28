import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from PIL import Image, ImageTk  # pip install pillow

# ----- Load tasks from file -----
TASK_FILE = "tasks.json"
tasks = []
completed_tasks = []

def load_tasks():
    global tasks, completed_tasks
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, dict):
                tasks = data.get("tasks", [])
                completed_tasks = data.get("completed", [])
            elif isinstance(data, list):  # fallback for old format
                tasks = data
                completed_tasks = []


def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump({"tasks": tasks, "completed": completed_tasks}, f, indent=2)

# ----- Main Window -----
root = tk.Tk()
root.title("Your Task")
root.geometry("500x650")

# Background image
bg_image = Image.open("bg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image.resize((500, 650)))

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Title
title_label = tk.Label(root, text="YOUR TASK", font=("Helvetica", 18, "bold"), bg="#ffffff")
title_label.pack(pady=15)

# Task frames
task_frame = tk.Frame(root, bg="#ffffff")
task_frame.pack(pady=5)

completed_label = tk.Label(root, text="COMPLETED TASKS", font=("Helvetica", 14, "bold"), bg="#ffffff")
completed_frame = tk.Frame(root, bg="#ffffff")

def update_task_display():
    # Clear current content
    for widget in task_frame.winfo_children():
        widget.destroy()
    for widget in completed_frame.winfo_children():
        widget.destroy()

    # Display active tasks
    for index, task in enumerate(tasks):
        task_row = tk.Frame(task_frame, bg="#ffffff")
        task_row.pack(pady=5, fill='x', padx=10)

        full_text = f"{task['desc']} | {task['date']} {task['time']}"
        task_label = tk.Label(task_row, text=full_text, font=("Arial", 11), anchor='w', width=30, bg="#ffffff")
        task_label.pack(side='left')

        tk.Button(task_row, text="🗑", command=lambda i=index: delete_task(i)).pack(side='right', padx=5)
        tk.Button(task_row, text="✔️", command=lambda i=index: mark_done(i)).pack(side='right', padx=5)
        tk.Button(task_row, text="✏️", command=lambda i=index: edit_task(i)).pack(side='right', padx=5)

    # Display completed tasks
    if completed_tasks:
        completed_label.pack(pady=(20, 5))
        completed_frame.pack()
        for task in completed_tasks:
            full_text = f"✔️ {task['desc']} | {task['date']} {task['time']}"
            completed_row = tk.Frame(completed_frame, bg="#ffffff")
            completed_row.pack(pady=2, fill='x', padx=10)
            tk.Label(completed_row, text=full_text, font=("Arial", 10), anchor='w', bg="#ffffff", fg="gray").pack(side='left')

def delete_task(index):
    del tasks[index]
    save_tasks()
    update_task_display()

def mark_done(index):
    completed_tasks.append(tasks.pop(index))  # Move task to completed
    save_tasks()
    update_task_display()

def edit_task(index):
    new_desc = simpledialog.askstring("Edit Task", "Update task description:", initialvalue=tasks[index]["desc"])
    if new_desc:
        tasks[index]["desc"] = new_desc
        save_tasks()
        update_task_display()

# ----- Add Task Window -----
def open_add_task_window():
    def save_task():
        date = date_entry.get()
        time = time_entry.get()
        desc = desc_entry.get("1.0", tk.END).strip()

        if desc:
            tasks.append({"date": date, "time": time, "desc": desc})
            save_tasks()
            update_task_display()
            add_win.destroy()
        else:
            messagebox.showwarning("Warning", "Task description cannot be empty!")

    add_win = tk.Toplevel(root)
    add_win.title("Add Task")
    add_win.geometry("300x250")
    add_win.configure(bg="#ffffff")

    tk.Label(add_win, text="Date:", bg="#ffffff").pack(pady=(10, 0))
    date_entry = tk.Entry(add_win)
    date_entry.pack()

    tk.Label(add_win, text="Time:", bg="#ffffff").pack(pady=(10, 0))
    time_entry = tk.Entry(add_win)
    time_entry.pack()

    tk.Label(add_win, text="Task Description:", bg="#ffffff").pack(pady=(10, 0))
    desc_entry = tk.Text(add_win, height=4, width=25)
    desc_entry.pack()

    btn_frame = tk.Frame(add_win, bg="#ffffff")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Cancel", command=add_win.destroy).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Done", command=save_task).grid(row=0, column=1, padx=5)

# Add Task Button
add_button = tk.Button(root, text="+", font=("Arial", 20), width=4, bg="#D8BFD8", command=open_add_task_window)
add_button.pack(pady=10)

# Load and display
load_tasks()
update_task_display()

root.mainloop()

