from tkinter import Label
from PIL import Image, ImageTk
from path_choice_screen import make_path_choice_screen


def make_adventure_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    adventure1_image_proto = Image.open(r"Images/adventure1_proto.png")
    adventure1_image = adventure1_image_proto.resize((400, 700), Image.LANCZOS)
    adventure1_image = ImageTk.PhotoImage(adventure1_image)
    adventure1_button = Label(venster, text="De bergen in", image=adventure1_image, compound="top")
    adventure1_button.image = adventure1_image
    adventure1_button.bind("<Button-1>", lambda click_event: make_path_choice_screen(venster))
    adventure1_button.place(relx=0.2, rely=0.45, anchor="center")

    adventure2_image_proto = Image.open(r"Images/adventure2_proto.png")
    adventure2_image = adventure2_image_proto.resize((400, 700), Image.LANCZOS)
    adventure2_image = ImageTk.PhotoImage(adventure2_image)
    adventure2_button = Label(venster, text="Het bos in", image=adventure2_image, compound="top")
    adventure2_button.image = adventure2_image
    adventure2_button.bind("<Button-1>", lambda click_event:make_path_choice_screen(venster))
    adventure2_button.place(relx=0.5, rely=0.45, anchor="center")

    adventure3_image_proto = Image.open(r"Images/adventure3_proto.png")
    adventure3_image = adventure3_image_proto.resize((400, 700), Image.LANCZOS)
    adventure3_image = ImageTk.PhotoImage(adventure3_image)
    adventure3_button = Label(venster, text="De rivier op", image=adventure3_image, compound="top")
    adventure3_button.image = adventure3_image
    adventure3_button.bind("<Button-1>", lambda click_event: make_path_choice_screen(venster))
    adventure3_button.place(relx=0.8, rely=0.45, anchor="center")
