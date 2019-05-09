import tkinter as tk

# create a window object
window = tk.Tk()

# title
window.title('dryang window title')

# window size
window.geometry('500x300')

# set a label
# note: bg is background font 
l = tk.Label(window, text = "input text here for label", bg = 'red', font=('Arial', 12), width=30, height=2)

# palce the label
# pack() or place()
l.pack()

# main loop
window.mainloop()