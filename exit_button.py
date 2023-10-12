from tkinter import Label
from PIL import Image, ImageTk

def make_exit_button(venster):
    character_imagesize_x = 25
    character_imagesize_y = 25

    original_image = Image.open(r"images/prohibit_sign.png")
    resized_image = original_image.resize(
        (character_imagesize_x, character_imagesize_y), Image.LANCZOS)
    character_slot_1_image = ImageTk.PhotoImage(resized_image)

    home_button = Label(venster, image=character_slot_1_image, bg="black")
    home_button.image = character_slot_1_image
    home_button.bind("<Button-1>", lambda click_event: exit())
    home_button.place(relx=0.965, rely=0.05, anchor="center")