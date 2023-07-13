from tkinter import *
from tkinter.messagebox import *

class Login(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Login')
        self.master.geometry('400x100+600+220')
        self.create_widgets()

    def create_widgets(self):
        self.var = IntVar()

        lbl_login = Label(self.master, text='Login').grid(row=0, column=0, padx=10)
        lbl_password = Label(self.master, text='Password').grid(row=1, column=0, padx=10)

        self.entry_login = Entry(self.master, bd=5)
        self.entry_login.grid(row=0, column=1, padx=10)

        self.entry_password = Entry(self.master, bd=5, show='*')
        self.entry_password.grid(row=1, column=1, padx=10)

        self.check_btn = Checkbutton(self.master, text='Show password', variable=self.var, command=self.show)
        self.check_btn.grid(row=1, column=2, padx=5)

        self.btn_login = Button(self.master, text='Login', command=self.login)
        self.btn_login.grid(row=2, column=2)


    def login(self):
        log = self.entry_login.get()
        psw = self.entry_password.get()

        if log == 'Admin' and psw == 'admin':
            self.master.withdraw()
            self.menu_window = Menu(self.master)
            self.menu_window.return_to_login = self.return_to_login

    def show(self):
        if self.var.get() == 1:
            self.entry_password['show'] = ''
        else:
            self.entry_password['show'] = '*'

    def return_to_login(self):

        self.master.deiconify()



class Menu(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title('Menu')
        self.geometry('300x400+600+220')
        self.create()

    def create(self):
        lbl = Label(self, text='Logged').pack()
        btn = Button(self, text='Return', command=self.return_to_login).pack()

    def return_to_login(self):
        self.destroy()
        self.return_to_login()


if __name__ == '__main__':
    root = Tk()
    log = Login(root)
    log.mainloop()
