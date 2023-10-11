from tkinter import Label
from PIL import Image, ImageTk


def goto_screen_select_character(venster):
    from character_selection import make_character_selection_screen
    make_character_selection_screen(venster)


def make_splash_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    orignial_image = Image.open(r"Images/testbutton.png")

    voorbeeld_image = ImageTk.PhotoImage(orignial_image)

    start_button = Label(venster, text="Choose your character", height=80, width=200, image=voorbeeld_image, compound="center")
    start_button.image = voorbeeld_image

    start_button.bind("<Button-1>", lambda click_event: goto_screen_select_character(venster))


    #Pack-Here
    start_button.pack(anchor="n", pady=300)