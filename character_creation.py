from tkinter import Label
from PIL import Image, ImageTk


def make_character_creation_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    original_image = Image.open(r"Images/stickman_echt.png")
    voorbeeld_image = ImageTk.PhotoImage(original_image)

    start_button = Label(venster, text="Create new character", image=voorbeeld_image, compound="bottom")
    start_button.image = voorbeeld_image
    # start_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_button.place(relx=0.35, rely=0.4, anchor="center")

    start_button = Label(venster, text="Choose existing character", image=voorbeeld_image, compound="bottom")
    start_button.image = voorbeeld_image
    # start_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_button.place(relx=0.65, rely=0.4, anchor="center")