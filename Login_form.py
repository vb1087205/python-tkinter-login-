import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "12345":
        messagebox.showinfo(
            "LOGIN SUCCESSFULLY!",
            "Welcome Admin!"
        )
    else:
        messagebox.showerror(
            "LOGIN FAILED!",
            "Invalid Username and Password!"
        )


root = tk.Tk()
root.title("Login Form")
root.geometry("400x450")
root.configure(bg="#eaf2f8")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="USER LOGIN",
    font=("Arial", 22, "bold"),
    bg="#eaf2f8",
    fg="#123c69"
)
title_label.pack(pady=20)


subtitle_label = tk.Label(
    root,
    text="Please enter your account details",
    font=("Arial", 10),
    bg="#eaf2f8",
    fg="gray"
)
subtitle_label.pack(pady=5)


username_label = tk.Label(
    root,
    text="Username",
    font=("Arial", 12, "bold"),
    bg="#eaf2f8",
    fg="black"
)
username_label.pack(pady=5)

username_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25
)
username_entry.pack(pady=5)


password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 12, "bold"),
    bg="#eaf2f8",
    fg="black"
)
password_label.pack(pady=5)

password_entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=25,
    show="*"
)
password_entry.pack(pady=5)

login_button = tk.Button(
    root,
    text="LOG IN",
    font=("Arial", 12, "bold"),
    bg="#89c800",
    fg="white",
    width=20,
    height=2,
    command=login
)
login_button.pack(pady=25)


footer_label = tk.Label(
    root,
    text="Python Tkinter Login System",
    font=("Arial", 9),
    bg="#eaf2f8",
    fg="gray"
)
footer_label.pack(pady=5)

root.mainloop()
