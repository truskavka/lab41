import tkinter as tk
from tkinter import messagebox


# Функції для операцій
def add():
    try:
        result = float(entry1.get()) + float(entry2.get())
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення")


def subtract():
    try:
        result = float(entry1.get()) - float(entry2.get())
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення")


def multiply():
    try:
        result = float(entry1.get()) * float(entry2.get())
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення")


def divide():
    try:
        denominator = float(entry2.get())
        if denominator == 0:
            raise ZeroDivisionError
        result = float(entry1.get()) / denominator
        result_label.config(text="Результат: " + str(result))
    except ZeroDivisionError:
        messagebox.showerror("Помилка", "Ділення на нуль неможливе")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть числові значення")


# Налаштування вікна
root = tk.Tk()
root.title("Калькулятор")

# Поля для вводу
entry1 = tk.Entry(root, width=10)
entry2 = tk.Entry(root, width=10)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Текст для полів
tk.Label(root, text="Перше число:").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Друге число:").grid(row=1, column=0, padx=5, pady=5)

# Кнопки для операцій
tk.Button(root, text="+", width=5, command=add).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="-", width=5, command=subtract).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="*", width=5, command=multiply).grid(row=2, column=2, padx=5, pady=5)
tk.Button(root, text="/", width=5, command=divide).grid(row=2, column=3, padx=5, pady=5)

# Поле для відображення результату
result_label = tk.Label(root, text="Результат: ")
result_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

# Запуск інтерфейсу
root.mainloop()
