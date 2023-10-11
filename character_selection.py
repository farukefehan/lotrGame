from tkinter import Label
from PIL import Image, ImageTk


def goto_adventure_selection_screen(venster):
    from Avonturen_selection import make_adventure_selection_screen
    make_adventure_selection_screen(venster)


def goto_character_creation(venster):
    from character_creation import make_character_creation_screen
    make_character_creation_screen(venster)


def make_character_selection_screen(venster):
    from main import kill_all_children, generate_background
    kill_all_children(venster)
    generate_background(venster)


    menu_button_image_proto = Image.open(r"Images/testbutton.png")
    menu_button_image = ImageTk.PhotoImage(menu_button_image_proto)

    template_character1_image_proto = Image.open(r"Images/hobbit_male.png")
    template_character1_image = template_character1_image_proto.resize((200, 200), Image.LANCZOS)
    template_character1_image = ImageTk.PhotoImage(template_character1_image)
    template_character1_button = Label(venster, text="Template character 1 \n Male Hobbit", image=template_character1_image, compound="bottom")
    template_character1_button.image = template_character1_image
    template_character1_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    template_character1_button.place(relx=0.3, rely=0.4, anchor="center")

    template_character2_image_proto = Image.open(r"Images/elf_male.png")
    template_character2_image = template_character2_image_proto.resize((200, 200), Image.LANCZOS)
    template_character2_image = ImageTk.PhotoImage(template_character2_image)
    template_character2_button = Label(venster, text="Template character 1 \n Male Elf", image=template_character2_image, compound="bottom")
    template_character2_button.image = template_character2_image
    template_character2_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    template_character2_button.place(relx=0.5, rely=0.4, anchor="center")

    template_character3_image_proto = Image.open(r"Images/dwarf_male.png")
    template_character3_image = template_character3_image_proto.resize((200, 200), Image.LANCZOS)
    template_character3_image = ImageTk.PhotoImage(template_character3_image)
    template_character3_button = Label(venster, text="Template character 1 \n Male Dwarf", image=template_character3_image, compound="bottom")
    template_character3_button.image = template_character3_image
    template_character3_button.bind("<Button-1>", lambda click_event: goto_adventure_selection_screen(venster))
    template_character3_button.place(relx=0.7, rely=0.4, anchor="center")

    start_button4 = Label(venster, text="User created characters", image=menu_button_image, compound="center")
    start_button4.image = menu_button_image
    start_button4.bind("<Button-1>", lambda click_event: goto_character_creation(venster))
    start_button4.place(relx=0.5, rely=0.6, anchor="center")



