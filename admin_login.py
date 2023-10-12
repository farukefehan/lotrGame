import tkinter.font
from tkinter import Entry, Label, Frame, Button
from PIL import Image, ImageTk

import character_selection
from end_screen import make_end_screen_dead

admin_mode = False


def admin_login(venster):
    global admin_mode
    from main import kill_all_children
    kill_all_children(venster)

    password = "kekw"

    frame1 = Frame(venster, width=1000, height=800, borderwidth=5, relief="raised")
    frame1.pack(anchor="center", pady=100)
    frame1.propagate(False)

    admin_login_title_label_font = tkinter.font.Font(family="Blackadder ITC", size=80, weight="bold")
    admin_login_title_label = Label(frame1, text="Admin login", font=admin_login_title_label_font, relief="groove")
    admin_login_title_label.pack(side="top", fill="x")

    voorbeeld_image = Image.open("images/testbutton.png")
    voorbeeld_image = ImageTk.PhotoImage(voorbeeld_image)

    original_image = Image.open("images/draakje_schattig.png", mode="r")
    resized_image = original_image.resize(
        (1000, 500), Image.LANCZOS)
    final_image = ImageTk.PhotoImage(resized_image)

    dragon_image = Label(frame1, image=final_image)
    dragon_image.image = final_image
    dragon_image.pack(fill="x", side="top")

    admin_login_title_label_font = tkinter.font.Font(family="Blackadder ITC", size=30, weight="bold")

    voer_wachtwoord_in_label = Label(frame1, text="Wat is het wachtwoord?", font=admin_login_title_label_font)
    voer_wachtwoord_in_label.pack(anchor="center")

    login_button = Button(frame1, text="Login", image=voorbeeld_image, compound="center", bg="#603000",
                         fg="black", relief="raised")
    login_button.image = voorbeeld_image
    login_button.pack(side="right", anchor="se")

    user_input = Entry(frame1, bd=1, font=admin_login_title_label_font, width=50)
    user_input.pack(side="left", anchor="sw", fill="x")

    login_button.bind("<Button-1>", lambda click_event: check_check(venster, user_input, password))

    from home_button import make_home_button
    make_home_button(venster)

def check_check(root, box, password):
    global admin_mode
    if box.get() == password:
        print("Admin logged in!")
        admin_mode = True
        character_selection.make_character_selection_screen(root)
    else:
        make_end_screen_dead(root, "De draak zet je in vuur en vlam!")


def check_admin_mode():
    return admin_mode


def verander_label_text(label, tekst):
    label["text"] = tekst
