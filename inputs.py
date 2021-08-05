from tkinter import *

root = Tk()
e = Entry(root, width=50, bg="maroon", fg="white")
e.insert(0,"Enter your name")
e.pack()


# borderwidth=50
def clickme():
    name=e.get()
    mylabel = Label(root, text=name)
    mylabel.pack()





button = Button(text="click me",  command=clickme)
button.pack()

root.mainloop()
