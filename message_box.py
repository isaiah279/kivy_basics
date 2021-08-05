from tkinter import *
from tkinter import messagebox

root = Tk()


def popup():
    messagebox.showinfo("Alert", "this is the mesaage").pack()


def popup2():
    messagebox.showwarning("Alert", "this is the mesaage").pack()


def popup3():
    messagebox.showerror("Alert", "this is the mesaage").pack()


def popup4():
    messagebox.askquestion("Alert", "do you what to exit?").pack()


def popup5():
    responce = messagebox.askyesno("Alert", "do you what to exit?")
    responce.pack()
    mylabel = Label(root, text=responce)
    mylabel.pack()


button = Button(root, text="click  me", command=popup5)
button.pack()
root.mainloop()
