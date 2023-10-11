from tkinter import Label
from PIL import Image, ImageTk


def make_character_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    label_2 = Label(venster, text="character selection screen")

    original_image = Image.open(r"Images/stickman_echt.png")

    voorbeeld_image = ImageTk.PhotoImage(original_image)

    # height = 700, width = 493,

    start_button = Label(venster, image=voorbeeld_image,
                         compound="center")
    start_button.image = voorbeeld_image

    # start_button.bind("<Button-1>", lambda click_event: goto_screen_select_character(venster))

    start_button.pack(anchor="n", pady="100")

    label_2.pack()