import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_display.delete(1.0, "end")
    text_display.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_display.delete(1.0, "end")
        text_display.insert(1.0, calculation)
    except (SyntaxError, ZeroDivisionError, NameError):
        clear_field()
        text_display.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_display.delete(1.0, "end")

# واجهة البرنامج
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

text_display = tk.Text(root, height=2, width=20, font=("Arial", 16))
text_display.grid(columnspan=4)

# تعريف الأزرار ومواقعها
buttons = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("C", 5, 0)
]

# إنشاء الأزرار باستخدام حلقة
for (text, row, col) in buttons:
    if text == "C":
        action = clear_field
    elif text == "=":
        action = evaluate_calculation
    else:
        action = lambda x=text: add_to_calculation(x)
    tk.Button(root, text=text, command=action, width=5, height=2, font=("Arial", 14)).grid(row=row, column=col)

root.mainloop()