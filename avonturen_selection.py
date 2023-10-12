from tkinter import Label
from PIL import Image, ImageTk
from paths_screen import start_adventure


def create_adventure_selection_image(venster, image_path, adventure_title, relx, rely, filepath, char_dict):
    adventure_image_proto = Image.open(image_path)
    adventure_image = adventure_image_proto.resize((400, 700), Image.LANCZOS)
    adventure_image = ImageTk.PhotoImage(adventure_image)
    adventure_button = Label(venster, text=adventure_title, image=adventure_image, compound="top",
                             bg="#603000", fg="white")
    adventure_button.image = adventure_image
    adventure_button.bind("<Button-1>", lambda click_event: start_adventure(venster, filepath, char_dict))
    adventure_button.place(relx=relx, rely=rely, anchor="center")


def make_adventure_selection_screen(venster, dict):
    from main import kill_all_children, generate_background
    kill_all_children(venster)
    generate_background(venster)
    from home_button import make_home_button
    make_home_button(venster)
    print(dict)

    create_adventure_selection_image(venster, r"adventures/geheimzinnigequest/rivendell.png",
                                     "De geheimzinnige Queeste", 0.2, 0.475,
                                     "adventures/goudenhal/de_gouden_hal.txt", dict)

    create_adventure_selection_image(venster, r"adventures/vermistedwergen/dwergen.png",
                                     "De verdwenen dwergen", 0.5, 0.475,
                                     "adventures/vermistedwergen/vermiste_dwergen.txt", dict)

    create_adventure_selection_image(venster, r"adventures/goudenhal/de gouden hal.png",
                                     "De Gouden Hal", 0.8, 0.475,
                                     "adventures/goudenhal/de_gouden_hal.txt", dict)
