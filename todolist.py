import tkinter as tk
from tkinter import messagebox
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []

        self.label = tk.Label(root, text="To-Do List", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Helvetica", 12), width=25)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="เพิ่มรายการ", width=15, command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), width=40, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="ลบรายการที่เลือก", width=15, command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.save_button = tk.Button(root, text="บันทึกรายการ", width=15, command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("คำเตือน", "กรุณากรอกงานก่อนเพิ่ม")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showwarning("คำเตือน", "กรุณาเลือกรายการที่จะลบ")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(task + "\n")
        messagebox.showinfo("บันทึกแล้ว", "บันทึกรายการเรียบร้อยแล้ว")

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r", encoding="utf-8") as f:
                self.tasks = [line.strip() for line in f.readlines()]
                self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
