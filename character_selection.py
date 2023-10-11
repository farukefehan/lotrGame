from tkinter import Label, Button
from PIL import Image, ImageTk


def goto_adventure_selection_screen(venster):
    from Avonturen_selection import make_adventure_selection_screen
    make_adventure_selection_screen(venster)


def make_character_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    label = Label(venster, text="Character 1")
    label.grid(row=0, column=0)

    original_image = Image.open(r"Images/stickman_echt.png")

    resized_image = original_image.resize((400, 400), Image.LANCZOS)
    voorbeeld_image = ImageTk.PhotoImage(resized_image)
    label_image = Label(venster, image=voorbeeld_image)
    label_image.image = voorbeeld_image
    button = Button(venster, image=label_image.image, command=lambda: goto_adventure_selection_screen(venster),
                    height=400, width=400)
    button.grid(row=1, column=0)

    label2 = Label(venster, text="Character 2")
    label2.grid(row=0, column=4)
    label_image = Label(venster, image=voorbeeld_image)
    label_image.image = voorbeeld_image
    button = Button(venster, image=label_image.image, command=lambda: goto_adventure_selection_screen(venster),
                    height=400, width=400)
    button.grid(row=1, column=4)
