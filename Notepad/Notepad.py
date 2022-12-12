from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

class Notepad():
    root=Tk()
    f= Frame(root)
    txt=Text(f, font="Calibri 14")
    file=None
    def __init__(self):        
        self.root.geometry("600x400")
        self.root.title("Notepad")
        self.root.wm_iconbitmap(r"C:\Users\_Karan_\Documents\Python\Notepad\notepad.ico")

        #scrollbar y
        scrolly=Scrollbar(self.f)
        scrolly.pack(fill=Y,side=RIGHT)
        scrolly.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=scrolly.set)
        self.txt.pack(fill=BOTH,expand=True)
        self.f.pack(fill=BOTH,expand=True)

        #Menu
        #File Menu
        mnubar=Menu(self.root)
        FileMenu=Menu(mnubar,tearoff=0)
        FileMenu.add_command(label="New",command=self.newfile)
        FileMenu.add_command(label="Save",command=self.savefile)
        FileMenu.add_command(label="Open",command=self.openfile)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit",command=self.quitfile)
        mnubar.add_cascade(label="File",menu=FileMenu)
        #Edit Menu
        EditMenu=Menu(mnubar,tearoff=0)
        EditMenu.add_command(label="Cut",command=self.cut)
        EditMenu.add_command(label="Copy",command=self.copy)
        EditMenu.add_command(label="Paste",command=self.paste)
        mnubar.add_cascade(label="Edit",menu=EditMenu)
        #Help Menu
        HelpMenu=Menu(mnubar,tearoff=0)
        HelpMenu.add_command(label="About",command=self.about)
        mnubar.add_cascade(label="Help",menu=HelpMenu)

        self.root.config(menu=mnubar)
    
    def newfile(self):
        self.root.title("Untitled - Notepad")
        self.file=None
        self.txt.delete(1.0,END)

    def openfile(self):
        self.file= askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.file=="":
            self.file=None
        else:
            self.root.title(os.path.basename(self.file) + " - Notepad")
            self.txt.delete(1.0,END)
            f=open(self.file,"r")
            self.txt.insert(1.0,f.read())
            f.close()
    
    def savefile(self):
        if self.file == None:
            self.file= asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if self.file=="":
                self.file=None
            else:
                f=open(self.file,"w")
                f.write(self.txt.get(1.0,END))
                f.close()
                self.root.title(os.path.basename(self.file) + " - Notepad")
        else:
            f=open(self.file,"w")
            f.write(self.txt.get(1.0,END))
            f.close()
            
    def quitfile(self):
        self.root.destroy()

    def cut(self):
        self.txt.event_generate("<<Cut>>")

    def copy(self):
        self.txt.event_generate("<<Copy>>")

    def paste(self):
        self.txt.event_generate("<<Paste>>")

    def about(self):
        tmsg.showinfo("About Notepad","Notepad Made By Karan")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    Notepad().run()