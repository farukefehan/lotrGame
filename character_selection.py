from tkinter import Label
from PIL import Image, ImageTk


def goto_adventure_selection_screen(venster):
    from avonturen_selection import make_adventure_selection_screen
    make_adventure_selection_screen(venster)


def goto_character_creation(venster):
    from character_creation import make_character_creation_screen
    make_character_creation_screen(venster)


def create_template_image_label(venster, image_path, race, relx_value, rely_value):
    template_character_image_proto = Image.open(image_path)
    template_character_image = template_character_image_proto.resize((200, 200), Image.LANCZOS)
    template_character_image = ImageTk.PhotoImage(template_character_image)
    template_character_button = Label(venster, text=race, image=template_character_image, compound="bottom",
                                      bg="#603000", fg="white")
    template_character_button.image = template_character_image
    template_character_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    template_character_button.place(relx=relx_value, rely=rely_value, anchor="center")


def make_character_selection_screen(venster):
    from main import kill_all_children
    kill_all_children(venster)

    from home_button import make_home_button
    make_home_button(venster)

    menu_button_image_proto = Image.open(r"images/testbutton.png")
    menu_button_image = ImageTk.PhotoImage(menu_button_image_proto)

    # Hobbit Template
    create_template_image_label(venster, "images/hobbit_male.png", "Hobbit", 0.3, 0.4)

    # Elf Template
    create_template_image_label(venster, "images/elf_male.png", "Elf", 0.5, 0.4)

    # Dwarf Template
    create_template_image_label(venster, "images/dwarf_male.png", "Dwarf", 0.7, 0.4)

    start_button4 = Label(venster, text="User created characters", image=menu_button_image, compound="center",
                          bg="#603000", fg="white")
    start_button4.image = menu_button_image
    start_button4.bind("<Button-1>", lambda click_event: goto_character_creation(venster))
    start_button4.place(relx=0.5, rely=0.6, anchor="center")
def characters_dictionary(file_path):

        characters = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    character = {"naam":parts[0],
                    "race": parts[1],
                    "describtion": parts[2],
                    "image": parts[3]}

                    characters.append(character)
        except FileNotFoundError:
            pass

        return characters

