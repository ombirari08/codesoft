import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.label = tk.Label(root, text="Password Length:")
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.complexity_label = tk.Label(root, text="Password Complexity:")
        self.complexity_label.pack(pady=5)

        self.complexity_var = tk.StringVar(root)
        self.complexity_var.set("Medium")
        self.complexity_menu = tk.OptionMenu(root, self.complexity_var, "Low", "Medium", "High", bg="#4d0099")
        self.complexity_menu.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(root, text="",bg="#4d0099",wraplength=300)
        self.password_label.pack()

    def generate_password(self):
        try:
            password_length = int(self.length_entry.get())
        except ValueError:
            self.password_label.config(text="Please enter a valid password length.")
            return

        password_characters = string.ascii_letters + string.digits + string.punctuation
        if self.complexity_var.get() == "Low":
            password_characters = string.ascii_letters + string.digits
        elif self.complexity_var.get() == "Medium":
            password_characters = string.ascii_letters + string.digits + string.punctuation

        if password_length <= 0:
            self.password_label.config(text="Password length must be greater than 0.")
        else:
            generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))
            self.password_label.config(text=f"Generated Password:\n{generated_password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
