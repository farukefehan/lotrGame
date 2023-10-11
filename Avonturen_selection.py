from tkinter import Label
from PIL import Image, ImageTk

def make_adventure_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)
    adventure1 = Label(venster, text="Avontuur 1")
    adventure2 = Label(venster, text="Avontuur 2")
    adventure3 = Label(venster, text="Avontuur 3")

    adventure1_image = Image.open(r"Images/adventure1_proto.jpg")

    voorbeeld_image = ImageTk.PhotoImage(adventure1_image)

    adventure1_button = Label(venster, image=adventure1_image,
                         compound="left")
    adventure2_button = Label(venster,
                         compound="middle")
    adventure3_button = Label(venster,
                         compound="right")

    adventure1.pack()
    adventure2.pack()
    adventure3.pack()