import tkinter as tk
from tkinter import ttk

class Main(tk.Tk):
    def __init__(self):

        # main setup
        super().__init__()
        self.title('Gamified To Do List')
        self.geometry('600x600')

        # frames
        Login_Frame(self)

        # run
        self.mainloop()

class Login_Frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.bind("<Button-1>", self.get_pos)

        self.login_widgets()


        self.pack(side="top", expand=True, fill="both")

    def login_widgets(self):

        console = ttk.Label(self, text = 'test', background = '#f07167')
        console.place(relx=0.45, rely=0.35, relwidth=0.20, relheight=0.20, anchor='center')

        entry = ttk.Entry(self)
        entry.place(relx=0.45, rely=0.50, anchor='center')

        console_btn = ttk.Button(self, text='Button')
        console_btn.place(relx=0.70, rely=0.50, anchor='center')


    def get_pos(self, event):
        relx = event.x / self.winfo_width()
        rely = event.y /self.winfo_height()

        print(f"{relx:.2f}, {rely:.2f}")


        

if __name__ == '__main__':
    app = Main()
    app