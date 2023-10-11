from tkinter import Label
from PIL import Image, ImageTk

def make_adventure_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)
    adventure1 = Label(venster, text="Avontuur 1")
    adventure2 = Label(venster, text="Avontuur 2")
    adventure3 = Label(venster, text="Avontuur 3")

    adventure1_image_proto = Image.open(r"Images/adventure1_proto.png")
    adventure1_image = adventure1_image_proto.resize((400, 400), Image.LANCZOS)
    adventure1_image = ImageTk.PhotoImage(adventure1_image)
    adventure2_image_proto = Image.open(r"Images/adventure2_proto.png")
    adventure2_image = adventure2_image_proto.resize((400, 400), Image.LANCZOS)
    adventure2_image = ImageTk.PhotoImage(adventure2_image)
    adventure3_image_proto = Image.open(r"Images/adventure3_proto.png")
    adventure3_image = adventure3_image_proto.resize((400, 400), Image.LANCZOS)
    adventure3_image = ImageTk.PhotoImage(adventure3_image)

    adventure1_button = Label(venster, image=adventure1_image, compound="bottom")
    adventure1_button.bind("<Button-1>", lambda click_event: (venster))
    adventure1_button.place(relx=0.3, rely=0.4, anchor="center")
    adventure1_button.image = adventure1_image

    adventure2_button = Label(venster, compound="center")
    adventure1_button.bind("<Button-1>", lambda click_event: (venster))
    adventure1_button.place(relx=0.5, rely=0.4, anchor="center")
    adventure2_button.image = adventure2_image
    adventure3_button = Label(venster, compound="center")
    adventure1_button.bind("<Button-1>", lambda click_event: (venster))
    adventure1_button.place(relx=0.7, rely=0.4, anchor="center")
    adventure3_button.image = adventure3_image

    adventure1_button.pack()
    adventure1.pack()
    adventure2.pack()
    adventure3.pack()

    #adventure1_button.bind("<Button-1>", lambda click_event: )