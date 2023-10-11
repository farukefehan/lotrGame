from tkinter import Label
from PIL import Image, ImageTk


def goto_screen_select_character(venster):
    from character_selection import make_character_selection_screen
    make_character_selection_screen(venster)


def goto_screen_admin_login(venster):
    from admin_menu import make_admin_menu
    make_admin_menu(venster)



def make_splash_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    orignial_image = Image.open(r"Images/testbutton.png")

    voorbeeld_image = ImageTk.PhotoImage(orignial_image)

    start_button = Label(venster, text="Choose your character", image=voorbeeld_image, compound="center")
    start_button.image = voorbeeld_image

    admin_button = Label(venster, text="Admin Login", image=voorbeeld_image, compound="center")

    start_button.bind("<Button-1>", lambda click_event: goto_screen_select_character(venster))
    admin_button.bind("<Button-1>", lambda click_event: goto_screen_admin_login(venster))



    #Pack-Here
    start_button.place(relx=0.5, rely=0.4, anchor="center")
    admin_button.place(relx=0.5, rely=0.5, anchor="center")
