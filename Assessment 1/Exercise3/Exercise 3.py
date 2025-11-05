#Exercise 3: Student Marks

try:
    from curses.textpad import Textbox
except Exception:
    Textbox = None
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import os
from turtle import title 

def load_student_marks(file_path="student_marks.txt"):
    students = []
    # resolve file path relative to this script so the external file is found reliably
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, file_path)

    if not os.path.isfile(full_path):
        # avoid showing a messagebox before the main Tk root exists
        print(f"Error: The file was not found at: {full_path}\nPlease ensure the file exists.")
        return students
    
    with open(full_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines[1:]:  # Skip header
        parts = line.strip().split(",")
        if len(parts) != 6:
            continue
        try:
            num = parts[0].strip()
            name = parts[1].strip()
            c1 = int(parts[2].strip())
            c2 = int(parts[3].strip())
            c3 = int(parts[4].strip())
            exam = int(parts[5].strip())
            # store as dict so other functions can use expected keys
            students.append({
                "number": num,
                "name": name,
                "coursework": [c1, c2, c3],
                "exam": exam
            })
        except (ValueError, IndexError):
            continue

    return students

def results(marks):
    cw = sum(marks["coursework"])
    exam = marks["exam"]
    total = cw + exam
    percentage = (total / 160) * 100
    if percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"
    return cw, exam, percentage, grade

def show():
    # populate tree with all students
    tree.delete(*tree.get_children())
    if not students:
        messagebox.showinfo("Info", "No student data available.")
        return

    for student in students:
        cw, exam, percentage, grade = results(student)
        tree.insert("", tk.END, values=(
            student["name"],
            student["number"],
            cw,
            exam,
            f"{percentage:.2f}%",
            grade,
        ))

def individual():
    if not students:
        messagebox.showinfo("Info", "No student data available.")
        return

    names = [student["name"] for student in students]
    name = simpledialog.askstring("Input", f"Enter student name from the following list:\n{', '.join(names)}")
    if not name:
        return

    tree.delete(*tree.get_children())
    found = None
    for student in students:
        if student["name"].lower() == name.lower():
            found = student
            break

    if found:
        cw, exam, percentage, grade = results(found)
        tree.insert("", tk.END, values=(
            found["name"],
            found["number"],
            cw,
            exam,
            f"{percentage:.2f}%",
            grade,
        ))
    else:
        messagebox.showinfo("Not found", f"Student '{name}' not found.")

def highest():
    tree.delete(*tree.get_children())
    if not students:
        messagebox.showinfo("Info", "No student data available.")
        return
    high = max(students, key=lambda s: (results(s)[2], sum(s["coursework"]), s["exam"]))
    cw, exam, percentage, grade = results(high)
    tree.insert("", tk.END, values=(
        high["name"],
        high["number"],
        cw,
        exam,
        f"{percentage:.2f}%",
        grade,
    ))

def lowest():
    tree.delete(*tree.get_children())
    if not students:
        messagebox.showinfo("Info", "No student data available.")
        return
    low = min(students, key=lambda s: (results(s)[2], sum(s["coursework"]), s["exam"]))
    cw, exam, percentage, grade = results(low)
    tree.insert("", tk.END, values=(
        low["name"],
        low["number"],
        cw,
        exam,
        f"{percentage:.2f}%",
        grade,
    ))


filename = "Marks.txt"
students = load_student_marks(filename)

root = tk.Tk()
root.title("Student Marks")
root.geometry("600x500")

title_label = tk.Label(root, text="Student Marks", font=("Arial", 16))
title_label.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn1 = tk.Button(btn_frame, text="Show All Students", command=show)
btn1.grid(row=0, column=0, padx=5)

btn2 = tk.Button(btn_frame, text="Individual Student", command=individual)
btn2.grid(row=0, column=1, padx=5)

btn3 = tk.Button(btn_frame, text="Highest Percentage", command=highest)
btn3.grid(row=0, column=2, padx=5)

btn4 = tk.Button(btn_frame, text="Lowest Percentage", command=lowest)
btn4.grid(row=0, column=3, padx=5)

btn5 = tk.Button(btn_frame, text="Exit", command=root.quit)
btn5.grid(row=0, column=4, padx=5)

text_frame = tk.Frame(root)
text_frame.pack(pady=10, fill=tk.BOTH, expand=True)

columns = ("name", "number", "cw", "exam", "perc", "grade")
tree = ttk.Treeview(text_frame, columns=columns, show="headings")
headings = ["Name", "Student Number", "Coursework Total", "Exam", "Percentage", "Grade"]
for col, hd in zip(columns, headings):
    tree.heading(col, text=hd)
    tree.column(col, anchor="center", width=100)

vsb = ttk.Scrollbar(text_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)

tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
vsb.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()