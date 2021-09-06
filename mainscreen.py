from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.font as font

root = Tk()
root.title("Starting")
root.geometry("500x500")

background_image = ImageTk.PhotoImage(Image.open("D:\\demo1.png"))
background_label = Label(root, image = background_image)
background_label.place(relwidth = 1, relheight =1)

def start():
    my_label.config(text = "Clicked")

button1 = Button(root, text = "START",bg = "#ADD8E6", fg = "#ff6f00", activeforeground = "#ADD8E6", activebackground = "#808080",borderwidth=10,command=start)
button1.place(relx = 0.44,rely = 0.85, relwidth = 0.2, relheight = 0.09)

my_label = Label(root,text='')
my_label.pack(pady=20)

mainloop()