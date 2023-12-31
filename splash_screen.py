from tkinter import Label
from PIL import Image, ImageTk


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


    original_image = Image.open("images/lotr.png", mode="r")
    resized_image = original_image.resize(
        (800, 400), Image.LANCZOS)
    head_image_resize = ImageTk.PhotoImage(resized_image)

    header_image = Label(image=head_image_resize)
    header_image.image = head_image_resize
    header_image.pack(side="top", pady=40)

    voorbeeld_image = make_image(r"images/testbutton.png")

    start_button = Label(venster, text="Begin het spel", image=voorbeeld_image, compound="center",
                         bg="#603000", fg="black")
    start_button.image = voorbeeld_image

    admin_button = Label(venster, text="Admin Login", image=voorbeeld_image, compound="center",
                         bg="#603000", fg="black")

    start_button.bind("<Button-1>", lambda click_event: goto_screen_select_character(venster))
    admin_button.bind("<Button-1>", lambda click_event: goto_screen_admin_login(venster))
    start_button.place(relx=0.5, rely=0.7, anchor="center")
    admin_button.place(relx=0.5, rely=0.8, anchor="center")

    from exit_button import make_exit_button
    make_exit_button(venster)
