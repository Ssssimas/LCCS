from tkinter import *
from tkinter import ttk
root = Tk()
frame = ttk.Frame(root, padding=100)
frame.grid()
ttk.Label(frame, text="Hello World!").grid(column=10, row=0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=10, row=0)
root.mainloop()