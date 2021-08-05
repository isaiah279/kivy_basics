from tkinter import *

root = Tk()
mylabel = Label(root, text="hello world")
mylabel2 = Label(root, text="my name is martin leon")
mylabel.grid(row=0, column=0)
mylabel2.grid(row=1, column=1)

root.mainloop()
