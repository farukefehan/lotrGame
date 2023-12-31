from tkinter import Label, Frame, Button
from PIL import Image, ImageTk

from admin_login import check_admin_mode
from end_screen import make_end_screen_dead, make_end_screen_success
from read_adventure import read_adventure

adventure = []
character_dict = {}
amount_of_checkpoints = 0
checkpoints_got = 0
admin_mode = False

def start_adventure(venster, file_name, dict):
    global adventure, character_dict, amount_of_checkpoints,checkpoints_got, admin_mode
    amount_of_checkpoints = 0
    checkpoints_got = 0
    character_dict = dict
    adventure = read_adventure(file_name)
    # print(adventure[0])
    amount_of_checkpoints = adventure.pop(0)
    first_screen = adventure[0]
    admin_mode = check_admin_mode()
    # print(f"admin: {admin_mode}")
    generate_screen(venster, first_screen)


def resize_image(file_path):
    # image_settings_characters
    character_imagesize_x = 400
    character_imagesize_y = 700

    original_image = Image.open(file_path, mode="r")
    resized_image = original_image.resize(
        (character_imagesize_x, character_imagesize_y), Image.LANCZOS)
    final_image = ImageTk.PhotoImage(resized_image)
    return final_image


def generate_screen(venster, screen_dict):
    global adventure
    global character_dict
    root = venster
    from main import kill_all_children
    kill_all_children(root)

    from home_button import make_home_button
    make_home_button(venster)

    character_slot_1_image = resize_image(character_dict['image'])

    character_slot_2_image = resize_image(screen_dict['image'])

    character_slot_1 = Label(root, image=character_slot_1_image, borderwidth=5, relief="raised")
    character_slot_1.image = character_slot_1_image
    character_slot_1.pack(anchor="nw", side="left", pady=100, padx=(10, 10))

    character_slot_2 = Label(root, image=character_slot_2_image, borderwidth=5, relief="raised")
    character_slot_2.image = character_slot_2_image
    character_slot_2.pack(anchor="ne", side="right", pady=100, padx=(10, 10))
    create_buttons(screen_dict, root)


def create_buttons(screen_dict, root):
    global checkpoints_got, amount_of_checkpoints
    frame1 = Frame(root, width=1000, height=800, borderwidth=5, relief="raised")
    frame1.pack(anchor="center", pady=100)
    frame1.propagate(False)

    frame2 = Frame(frame1, borderwidth=5, relief="raised", height=360)
    frame2.pack(side="top", anchor="center", fill="x")
    frame2.propagate(False)

    min_space_label = Label(frame2, width=1, height=1, bg="black", text=f"{checkpoints_got}/{amount_of_checkpoints}", fg="white")
    min_space_label.pack(anchor="n", fill="x")

    option_list = screen_dict['options']

    for option in option_list:
        if admin_mode is True:
            button_text = f"{option['text']} {option['admin']}"
        else:
            button_text = f"{option['text']}"
        option_button = Button(frame2, text=button_text, height=4, pady=1, padx=1,
                               borderwidth=1, relief="raised", anchor="w", justify="left",
                               command=lambda x=root, y=option['action'], z=option['death_message']:
                               take_action(x, y, z))
        option_button.pack(anchor="w", pady=1, padx=1, fill="x")

    question_label = Label(frame1, text=screen_dict['question'], anchor="center", compound="center",
                           borderwidth=2, relief="sunken")
    question_label.pack(expand=1)


def take_action(root, code_string, death_message):
    global adventure, checkpoints_got, amount_of_checkpoints
    if code_string.find("goto") != int("-1"):
        action = code_string.replace("goto", "")
        if action == "Died":
            make_end_screen_dead(root, death_message)
        elif action == "Win":
            checkpoints_got += 1
            make_end_screen_success(root, death_message)
        else:
            if death_message == "CP":
                checkpoints_got += 1
            action = int(action)
            # print(action)
            generate_screen(root, adventure[action])
