import tkinter as tk 
from PIL import Image

# create a window
window = tk.Tk()
window.title('Input ur title here')
window.geometry('800x650')  

# image file dir
pic_dir = 'C:\\Users\\lamborghni\\Documents\\GitHub\\allinone\\python\\app_2\\pic.gif'

# use PIL to read size 
# read image size
pic_1 = Image.open(pic_dir)
(x, y) = pic_1.size 

# create a canvas
canvas = tk.Canvas(window, bg = 'red', width = 800, height = 600)
pic_tk = tk.PhotoImage(file = pic_dir) 

# image position(x/2+10,10)
# n is anche position anchor = n s w e nw sw se ne center
image = canvas.create_image(x/2 + 10, y/2 + 10, anchor = 'center', image = pic_tk)

# create points
x0, y0, x1, y1 = 10, 10, 150, 150

# draw a line
line = canvas.create_line(x0 + x, y0, x1 + x, y1)

# draw a oval
oval = canvas.create_oval(x0 + 0.5*x, y0 + 1.5*y, x1 + 0.5*x, y1 + 1.5*y, fill = 'red')

# draw a arc
arc = canvas.create_arc(x0 + x, y0 + 50, x1 + x, y1 + 50, start = 0, extent = 180)

# draw a rect
rect = canvas.create_rectangle(x0, y0 + y + 20, x1, y1 + y + 20, fill = 'black')

# place canvas
canvas.pack()

def moveit():
    # move rect by x = 50 y = 50
    canvas.move(rect, 50, 50) 
 
# move rect
tk.Button(window, text = 'move item', command = moveit).pack()
 
# loop main window
window.mainloop()