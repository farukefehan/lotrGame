from tkinter import Label, Canvas
from PIL import Image, ImageTk


def goto_home_button(venster):
    from home_button import make_home_button
    make_home_button(venster)



def goto_screen_select_character(venster):
    from character_selection import make_character_selection_screen
    make_character_selection_screen(venster)


def goto_screen_admin_login(venster):
    from admin_login import admin_login
    admin_login(venster)


def make_image(image_path):
    original_image = Image.open(image_path)
    return ImageTk.PhotoImage(original_image)


def make_splash_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    voorbeeld_image = make_image(r"images/testbutton.png")
    goto_home_button(venster)


    start_button = Label(venster, text="Choose your character", image=voorbeeld_image, compound="center", bg="#603000", fg="black")
    start_button.image = voorbeeld_image

    admin_button = Label(venster, text="Admin Login", image=voorbeeld_image, compound="center", bg="#603000", fg="black")

    start_button.bind("<Button-1>", lambda click_event: goto_screen_select_character(venster))
    admin_button.bind("<Button-1>", lambda click_event: goto_screen_admin_login(venster))
    start_button.place(relx=0.5, rely=0.4, anchor="center")
    admin_button.place(relx=0.5, rely=0.5, anchor="center")
