from tkinter import Label
from PIL import Image, ImageTk


def make_character_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    label_2 = Label(venster, text="character selection screen")

    label_2.pack()