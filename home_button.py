from tkinter import Label
from PIL import Image, ImageTk


def goto_splash_screen(venster):
    from main import make_splash_screen
    make_splash_screen(venster)


def make_home_button(venster):
    character_imagesize_x = 50
    character_imagesize_y = 50

    original_image = Image.open(r"images/prohibit_sign.png")
    resized_image = original_image.resize((character_imagesize_x, character_imagesize_y), Image.LANCZOS)
    character_slot_1_image = ImageTk.PhotoImage(resized_image)

    home_button = Label(venster, image=character_slot_1_image, compound="bottom", bg="#603000", fg="white")
    home_button.image = character_slot_1_image
    home_button.bind("<Button-1>", lambda click_event: goto_splash_screen(venster))
    home_button.place(relx=0.975, rely=0.95, anchor="center")
