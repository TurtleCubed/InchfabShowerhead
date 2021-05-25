import tkinter as tk
import tkinter.ttk as ttk


class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame2 = ttk.Frame(self.toplevel1)
        self.canvas1 = tk.Canvas(self.frame2)
        self.canvas1.pack(side='top')
        self.frame2.configure(height='200', width='200')
        self.frame2.pack(side='top')
        self.toplevel1.configure(height='200', width='200')

        self.labels = [None]*10
        self.labels[0] = self.canvas1.create_image(50, 50, image=tk.PhotoImage(file='..\\blank.png'))

        # Main widget
        self.mainwindow = self.toplevel1


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = NewprojectApp()
    app.run()

