from tkinter import Label
from PIL import *
from PIL import Image, ImageTk


def make_splash_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    orignial_image = Image.open(r"testbutton.png")

    voorbeeld_image = ImageTk.PhotoImage(orignial_image)

    start_button = Label(venster, text="START", height=80, width=200, image=voorbeeld_image, foreground="BLACK")
    start_button.image = voorbeeld_image


    #Pack-Here
    start_button.pack(anchor="n", pady=300)