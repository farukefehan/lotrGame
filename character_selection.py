from tkinter import Label, Button
from PIL import Image, ImageTk


def goto_adventure_selection_screen(venster):
    from Avonturen_selection import make_adventure_selection_screen
    make_adventure_selection_screen(venster)


def make_character_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    original_image = Image.open(r"Images/stickman_echt.png")
    voorbeeld_image = ImageTk.PhotoImage(original_image)

    start_button = Label(venster, text="Character 1", image=voorbeeld_image, compound="bottom")
    start_button.image = voorbeeld_image
    start_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_button.place(relx=0.3, rely=0.4, anchor="center")

    start_button2 = Label(venster, text="Character 2", image=voorbeeld_image, compound="bottom")
    start_button2.image = voorbeeld_image
    start_button2.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_button2.place(relx=0.5, rely=0.4, anchor="center")

    start_button3 = Label(venster, text="Character 3", image=voorbeeld_image, compound="bottom")
    start_button3.image = voorbeeld_image
    start_button3.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_button3.place(relx=0.7, rely=0.4, anchor="center")
