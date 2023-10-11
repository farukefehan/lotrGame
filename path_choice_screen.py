import math
from tkinter import Label, Frame
from PIL import Image, ImageTk

def make_path_choice_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)


    original_image = Image.open(r"Images/stickman_echt.png")
    resized_image = original_image.resize((400, 600), Image.LANCZOS)
    character_slot_1_image = ImageTk.PhotoImage(resized_image)

    character_slot_1 = Label(venster, image=character_slot_1_image, width=500, height=700)
    character_slot_1.image = character_slot_1_image

    choice_frame = Frame(venster, width=1100, height=800)
    label_choice_1 = Label(choice_frame, text="Choice 1", height=2, relief="raised")
    label_choice_2 = Label(choice_frame, text="Choice 2", height=2, relief="raised")
    label_choice_3 = Label(choice_frame, text="Choice 3", height=2, relief="raised")

    label_question = Label(choice_frame, text="Question Here", height=3, relief="raised")

    original_image = Image.open(r"Images/stickman_echt.png")
    resized_image = original_image.resize((400, 600), Image.LANCZOS)
    character_slot_2_image = ImageTk.PhotoImage(resized_image)

    label_choice_1.bind("<Button-1>", lambda click_event: goto_screen_select_character(venster))
    label_choice_2.bind("<Button-1>", lambda click_event: goto_screen_select_character(venster))
    label_choice_3.bind("<Button-1>", lambda click_event: goto_screen_select_character(venster))

    character_slot_2 = Label(venster, image=character_slot_2_image, width=500)
    character_slot_2.image = character_slot_2_image


    venster.grid()
    character_slot_1.grid(column=0, row=0)
    label_choice_1.pack(anchor="w")
    label_choice_2.pack(anchor="w")
    label_choice_3.pack(anchor="w")
    label_question.pack(anchor="s")
    choice_frame.grid(column=1, row=0, ipadx=200, pady=100)
    character_slot_2.grid(column=2, row=0)