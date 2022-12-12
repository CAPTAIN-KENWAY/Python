from tkinter import *


class calculator_gui(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("350x450")
        self.maxsize(350, 450)
        self.minsize(350, 450)
        self.title("Calculator - Made By Karan")
        self.config(background="white")


        self.scvalue = StringVar()
        self.scvalue.set("")
        self.f = Frame(self, bg="white")
        self.screen = Entry(
            self.f, textvariable=self.scvalue, font="Calibri 35 bold")
        Button(self.f, text='C', bg='orange', font="Calibri 25 bold",
               command=self.clear).pack(side=RIGHT,ipadx=12, padx=8)
        self.screen.pack(pady=5, padx=5)
        self.f.pack(padx=10, pady=10, anchor='w')


        self.f = Frame(self, bg="white")
        Button(self.f, text='9', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('9')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='8', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('8')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='7', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('7')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='+', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('+')).pack(ipadx=13, side=LEFT, padx=8)

        self.f.pack(padx=10, pady=10, anchor='w')
        self.f = Frame(self, bg="white")
        Button(self.f, text='6', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('6')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='5', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('5')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='4', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('4')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='-', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('-')).pack(ipadx=16, side=LEFT, padx=8)

        self.f.pack(padx=10, pady=10, anchor='w')
        self.f = Frame(self, bg="white")
        Button(self.f, text='3', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('3')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='2', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('2')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='1', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('1')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='*', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('*')).pack(ipadx=13, side=LEFT, padx=8)

        self.f.pack(padx=10, pady=10, anchor='w')
        self.f = Frame(self, bg="white")
        Button(self.f, text='=', bg='orange', font="Calibri 25 bold",
               command=self.equal).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='0', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('0')).pack(ipadx=12, side=LEFT, padx=8)

        Button(self.f, text='%', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('%')).pack(ipadx=10, side=LEFT, padx=8)

        Button(self.f, text='/', bg='orange', font="Calibri 25 bold",
               command=lambda: self.click('/')).pack(ipadx=14, side=LEFT, padx=8)

        self.f.pack(padx=10, pady=10, anchor='w')

    def click(self, n):
        self.screen.insert(END, n)
        self.screen.update()

    def equal(self):
        value = self.scvalue.get()
        if self.scvalue.get().isdigit():
            value = int(self.scvalue.get())
        else:
            try:
                value = eval(self.screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        self.scvalue.set(value)
        self.screen.update()

    def clear(self):
        self.scvalue.set("")
        self.screen.update()


if __name__ == '__main__':
    window = calculator_gui()
    window.mainloop()
