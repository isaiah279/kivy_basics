from tkinter import *

root = Tk()


def myclick():
    mylabel = Label(root, text="hello world")
    mylabel.pack()


mybutton = Button(root, text="click me", command=myclick, fg="red",bg="green").pack()
# state=DISABLED,
#  padx=50,
# pady=50
root.mainloop()
