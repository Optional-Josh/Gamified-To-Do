import os
import tkinter as tk
from tkinter import ttk

class Main(tk.Tk):
    def __init__(self):

        # main setup
        super().__init__()
        self.title('Gamified To Do List')
        self.configure(bg='#FF7F7F')
        height = 900
        width = 900
        x = (self.winfo_screenwidth()//2) - (width//2)
        y = (self.winfo_screenheight()//2) - (width//2) + (-50)
        self.geometry(f"{width}x{height}+{x}+{y}")

        # frames
        Login_Frame(self)

        # run
        self.mainloop()

class Login_Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.bind("<Button-1>", self.get_pos)

        self.login_widgets()


        self.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.7 ,anchor='center')

    def login_widgets(self):

        button_styles = ttk.Style()
        button_styles.configure("Login.TButton", font=('Arial, 15'), foreground="blue", background="white")


        ttk.Label(self, text = 'LOGIN', font=("Arial", 50)).place(relx=0.20, rely=0.10, anchor='center')

        ttk.Label(self, text = 'Username', font=('Arial', 20)).place(relx=0.33, rely=0.49, anchor='center')

        self.console = ttk.Label(self, text = 'Terminal', font=('Arial', 15))
        self.console.place(relx=0.50, rely=0.80, anchor='center')

        self.entry = ttk.Entry(self, width=15, font=('Arial',15))
        self.entry.place(relx=0.35, rely=0.55, anchor='center')

        console_btn = ttk.Button(self, text='Button', style="Login.TButton", command=self.user_login)
        console_btn.place(relx=0.65, rely=0.55, anchor='center')

    def user_login(self):
            entry_input = self.entry.get()

            folder_path = "C:\\Users\\Administrator\\Desktop\\Entire Files\\Programming\\Self-Taught Work\\Gamified To Do"
            file_name = f"{entry_input}.json"

            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                self.console.config(text=f'Username "{entry_input}" found! Opening now...')
            else:
                self.console.config(text=f'Username "{entry_input}" not found!')

    def get_pos(self, event):
        relx = event.x / self.winfo_width()
        rely = event.y /self.winfo_height()

        print(f"{relx:.2f}, {rely:.2f}")


        

if __name__ == '__main__':
    app = Main()
    app