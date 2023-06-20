import tkinter as tk

tasks = []

def add_task():
    global entry_task  # Declare entry_task as a global variable
    task = entry_task.get()
    if task:
        tasks.append(task)
        list_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def mark_task_complete():
    global list_tasks  # Declare list_tasks as a global variable
    selected_task = list_tasks.curselection()
    if selected_task:
        index = selected_task[0]
        list_tasks.delete(index)
        del tasks[index]

def main():
    global entry_task, list_tasks  # Declare entry_task and list_tasks as global variables

    root = tk.Tk()
    root.title("To-Do List")

    list_tasks = tk.Listbox(root, width=50)
    list_tasks.pack()

    entry_task = tk.Entry(root, width=50)
    entry_task.pack()

    btn_add_task = tk.Button(root, text="Add Task", command=add_task)
    btn_add_task.pack()

    btn_mark_complete = tk.Button(root, text="Mark Complete", command=mark_task_complete)
    btn_mark_complete.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
