from tkinter import Label
from PIL import Image, ImageTk


def goto_adventure_selection_screen(venster):
    from Avonturen_selection import make_adventure_selection_screen
    make_adventure_selection_screen(venster)


def goto_end_screen(venster):
    from end_screen import make_end_screen
    make_end_screen(venster, True)


def goto_character_creation(venster):
    from character_creation import make_character_creation_screen
    make_character_creation_screen(venster)


def make_character_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    original_image = Image.open(r"Images/stickman_echt.png")
    voorbeeld_image = ImageTk.PhotoImage(original_image)

    original_image = Image.open(r"Images/testbutton.png")
    voorbeeld_image2 = ImageTk.PhotoImage(original_image)



    start_button = Label(venster, text="Template character 1", image=voorbeeld_image, compound="bottom")
    start_button.image = voorbeeld_image
    start_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_button.place(relx=0.3, rely=0.4, anchor="center")

    start_button2 = Label(venster, text="Template character 2", image=voorbeeld_image, compound="bottom")
    start_button2.image = voorbeeld_image
    start_button2.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_button2.place(relx=0.5, rely=0.4, anchor="center")

    start_button3 = Label(venster, text="Template character 3", image=voorbeeld_image, compound="bottom")
    start_button3.image = voorbeeld_image
    start_button3.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_button3.place(relx=0.7, rely=0.4, anchor="center")

    start_button4 = Label(venster, text="User characters", image=voorbeeld_image2, compound="center")
    start_button4.image = voorbeeld_image2
    start_button4.bind("<Button-1>", lambda click_event: goto_character_creation(venster))
    start_button4.place(relx=0.5, rely=0.6, anchor="center")

