import tkinter.font
from tkinter import Entry, Label, Button
from PIL import Image, ImageTk






def admin_login(venster):
    from main import kill_all_children
    kill_all_children(venster)

    admin_mode = False

    admin_login_title_label_font = tkinter.font.Font(family="Blackadder ITC", size=80, weight="bold")
    admin_login_title_label = Label(venster, text="Admin login", font=admin_login_title_label_font)
    admin_login_title_label.place(relx=0.5, rely=0.3, anchor="center")

    voer_wachtwoord_in_label = Label(venster, text="Voer je wachtwoord in:")
    voer_wachtwoord_in_label.place(relx=0.5, rely=0.425, anchor="center")

    voorbeeld_image = Image.open("images/testbutton.png")

    login_button = Label(venster, text="Login", image=voorbeeld_image, compound="center", bg="#603000",
                         fg="black")
    start_button.image = voorbeeld_image



    login_button.bind("<Button-1>", lambda click_event: )

    login_button.place(relx=0.5, rely=0.4, anchor="center")



def check_admin_wachtwoord(user):
    print()





    # hello_world_label = Label(venster, text="Admin login")

    # button = Button(venster, text="Login",
    #                 command=lambda: verander_label_text(hello_world_label, gebruikers_input.get()))
    # gebruikers_input = Entry(venster, bd=1)




    # hello_world_label.place(relx=0.5, rely=0.3, anchor="center")
    # gebruikers_input.place(relx=0.5, rely=0.45, anchor="center")
    # button.place(relx=0.5, rely=0.5, anchor="center")


def verander_label_text(label, tekst):
    label["text"] = tekst
