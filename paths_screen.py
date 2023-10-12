from tkinter import Label, Frame
from PIL import Image, ImageTk
from read_adventure import read_adventure

def start_adventure(venster, file_name):
    read_adventure(file_name)
    first_screen = adventure[0]
    generate_screen(venster, first_screen)

def generate_screen(venster, screen_dict):
    root = venster
    from main import kill_all_children
    kill_all_children(root)

    #image_settings_characters
    character_imagesize_x = 400
    character_imagesize_y = 800

    original_image = Image.open(r"Images/stickman_echt.png")
    resized_image = original_image.resize((character_imagesize_x, character_imagesize_y), Image.LANCZOS)
    character_slot_1_image = ImageTk.PhotoImage(resized_image)

    character_slot_1 = Label(root, image=character_slot_1_image, borderwidth=5, relief="raised")
    character_slot_1.image = character_slot_1_image
    character_slot_1.pack(anchor="nw", side="left", pady=100, padx=(10, 10))

    character_slot_2 = Label(root, image=character_slot_1_image, borderwidth=5, relief="raised")
    character_slot_2.image = character_slot_1_image
    character_slot_2.pack(anchor="ne", side="right", pady=100, padx=(10, 10))
    create_buttons(screen_dict, root)


def create_buttons(screen_dict, root):
    frame1 = Frame(root, width=1000, height=800, borderwidth=5, relief="raised")
    frame1.pack(anchor="center", pady=100)
    frame1.propagate(0)

    frame2 = Frame(frame1, borderwidth=5, relief="raised", height=600)
    frame2.pack(side="top", anchor="center", fill="x")
    frame2.propagate(0)

    min_space_label = Label(frame2, width=10, height=10, bg="black")
    min_space_label.pack(anchor="n", fill="x")

    option_list = screen_dict['options']
    for option in option_list:
        option_button = Label(frame2, text=option['text'], height=5, pady=1, padx=1, borderwidth=1, relief="raised", anchor="w", justify="left")
        #bind here
        option_button.pack(anchor="w", pady=1, padx=1, fill="x")

    question_label = Label(frame1, text=screen_dict['question'], anchor="center", compound="center", borderwidth=2, relief="sunken")
    question_label.pack(expand=1)
