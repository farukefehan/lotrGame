from tkinter import Label
from PIL import Image, ImageTk

def make_adventure_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)
    adventure1 = Label(venster, text="Avontuur 1")