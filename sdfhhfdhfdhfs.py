import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Вход в систему")
root.geometry("300x300")
root.configure(bg="#CEEAD6")


def login():
    username = entry_username.get()
    password = entry_password.get()
    if password == username and password in ["teacher1", "teacher2", "techer3"]:
        messagebox.showinfo("Вход выполнен", "Добро пожаловать в ситсему, вы учитель")
    if password == username and password in ["parent1", "parent2", "parent3"]:
        messagebox.showinfo("Вход выполнен, Добро пожаловать в ситсему, вы родитель")
    if password == username and password in ["stud1", "stud2", "stud3"]:
        messagebox.showinfo("Вход выполнен", "Добро пожаловать в ситсему, вы студент")
    else:
        messagebox.showwarning("Ошибка", "Неверный логин или пороль")


def forgot_password():
    messagebox.showinfo("Вы забыли пороль?", "Окно восстановления пароля")


def register():
    messagebox.showinfo("Регистрация", "Вы находитесь в окне регистрации")


font_style = ("Arial", 12)

label_username = tk.Label(root, text="Логин:", bg="#f2f2f2", font=font_style)
label_username.pack(pady=(20, 0))

entry_username = tk.Entry(root, font=font_style)
entry_username.pack(pady=(0, 10))

label_password = tk.Label(root, text="Пароль:", bg="#f2f2f2", font=font_style)
label_password.pack(pady=(10, 0))

entry_password = tk.Entry(root, show="*", font=font_style)
entry_password.pack(pady=(0, 20))

button_login = tk.Button(root, text="Войти", command=login, font=font_style, bg="#4CAF50", fg="white")
button_login.pack(pady=(10, 5))

button_forgot = tk.Button(root, text="Забыли пароль?", command=forgot_password, font=font_style, bg="#A50E0E",
                          fg="white")
button_forgot.pack(pady=(5, 5))

button_register = tk.Button(root, text="Регистрация", command=register, font=font_style, bg="#FF9800", fg="white")
button_register.pack(pady=(5, 20))

root.mainloop()