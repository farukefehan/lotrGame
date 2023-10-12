import tkinter.font
from tkinter import Entry, Label
from PIL import Image, ImageTk
admin_mode = False


def admin_login(venster):
    global admin_mode
    from main import kill_all_children
    kill_all_children(venster)

    password = "kekw"

    admin_login_title_label_font = tkinter.font.Font(family="Blackadder ITC", size=80, weight="bold")
    admin_login_title_label = Label(venster, text="Admin login", font=admin_login_title_label_font)
    admin_login_title_label.place(relx=0.5, rely=0.3, anchor="center")

    voer_wachtwoord_in_label = Label(venster, text="Voer je wachtwoord in:")
    voer_wachtwoord_in_label.place(relx=0.5, rely=0.425, anchor="center")

    voorbeeld_image = Image.open("images/testbutton.png")
    voorbeeld_image = ImageTk.PhotoImage(voorbeeld_image)

    login_button = Label(venster, text="Login", image=voorbeeld_image, compound="center", bg="#603000",
                         fg="black")
    login_button.image = voorbeeld_image

    user_input = Entry(venster, bd=1)
    user_input.place(relx=0.5, rely=0.5, anchor="center")

    login_button.bind("<Button-1>", lambda click_event: check_admin_wachtwoord(user_input, password))


def check_check():

    if check_admin_wachtwoord(user_input, password):
        print("Thijs stinkt")
    else:
        print("Thijs very stinky")

    login_button.place(relx=0.5, rely=0.6, anchor="center")


def check_admin_wachtwoord(user_input, password):
    if user_input == password:
        admin_mode = True
        return admin_mode
    else:
        return False


def verander_label_text(label, tekst):
    label["text"] = tekst
