from PIL import Image, ImageTk
import tkinter as tk 
import tkinter.messagebox
import pickle

# create a image
window = tk.Tk()
window.title('Input ur title here')
# size is small x 
window.geometry('1080x800') 
 
# import a pic
canvas = tk.Canvas(window, width = 1080, height = 800, bg='green')

# image directory

image_dir = "C:/Users/Administrator/Documents/GitHub/allinone/python/app_2/anchor.png"
image_dir_1 = "C:/Users/lamborghni/Documents/GitHub/allinone/python/app_2/anchor.png"
image_pil = Image.open(image_dir_1)
(img_x, img_y) = image_pil.size

# tkinter only hangdle gif image 
# use PIL(jpg png) to convert
image_tk = ImageTk.PhotoImage(image_pil)

image = canvas.create_image(img_x/2+20, img_y/2 + 20, anchor = 'center', image = image_tk)
# pack value top, bottom, left, or right
canvas.pack(side = 'top')

# create a label 
tk.Label(window, text = 'Inpurt ur label here ',font =('Arial', 16)).place()
tk.Label(window, text = 'User name:', font = ('Arial', 14)).place(x = 20, y = img_y+80)
tk.Label(window, text = 'Password:', font = ('Arial', 14)).place(x = 20, y = img_y+130)
 
# input name
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable = var_usr_name, font = ('Arial', 14))
entry_usr_name.place(x = 140, y = img_y+80)

# input password
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable = var_usr_pwd, font = ('Arial', 14), show='*')
entry_usr_pwd.place(x = 140, y = img_y+130)
 
# def login button
def usr_login():
    # get value 
    pass
 
# def sign up function
def usr_sign_up():
    pass
 
# button position
btn_login = tk.Button(window, text = 'Login', command = usr_login)
btn_login.place(x = 120, y = img_y+170)
btn_sign_up = tk.Button(window, text = 'Sign up', command = usr_sign_up)
btn_sign_up.place(x = 200, y = img_y+170)
 
# loop main window
window.mainloop()