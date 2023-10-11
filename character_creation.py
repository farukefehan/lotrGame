from tkinter import Label, Entry, StringVar
from PIL import Image, ImageTk


def goto_character_creation(venster):
    from character_selection import make_character_selection_screen
    make_character_selection_screen(venster)


def make_character_creation_screen(venster):
    from main import kill_all_children, generate_background
    kill_all_children(venster)
    generate_background(venster)

    original_image = Image.open(r"Images/stickman_echt.png")
    voorbeeld_image = ImageTk.PhotoImage(original_image)

    start_button = Label(venster, text="Create new character", image=voorbeeld_image, compound="bottom", bg="#603000", fg="white")
    start_button.image = voorbeeld_image
    start_button.bind("<Button-1>", lambda click_event: make_new_character(venster))
    start_button.place(relx=0.35, rely=0.4, anchor="center")

    start_button = Label(venster, text="Choose existing character", image=voorbeeld_image, compound="bottom", bg="#603000", fg="white")
    start_button.image = voorbeeld_image
    # start_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    start_button.place(relx=0.65, rely=0.4, anchor="center")

    original_image2 = Image.open(r"Images/home_button.png")
    original_image2 = original_image2.resize((200, 200), Image.LANCZOS)
    voorbeeld_image2 = ImageTk.PhotoImage(original_image2)

    end_button2 = Label(venster, image=voorbeeld_image2, text="Back to character selection", compound="bottom", bg="#603000", fg="white")
    end_button2.image = voorbeeld_image2
    end_button2.bind("<Button-1>", lambda click_event: goto_character_creation(venster))
    end_button2.place(relx=0.5, rely=0.7, anchor="center")


def make_new_character(venster):
    entry_text = StringVar()
    start_button = Entry(venster, textvariable=entry_text)
    entry_text.set("Input name")
    start_button.place(relx=0.35, rely=0.6, anchor="center")

    entry_text = StringVar()
    start_button = Entry(venster, textvariable=entry_text)
    entry_text.set("Dit wordt een dropdown menu")
    start_button.place(relx=0.35, rely=0.65, anchor="center")
