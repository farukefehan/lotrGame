from tkinter import Entry, Label, Button
from PIL import Image, ImageTk






def admin_login(venster):
    from main import kill_all_children
    kill_all_children(venster)


    hello_world_label = Label(venster, text="Admin login")
    label2 = Label(venster, text="Voer je wachtwoord in:")
    button = Button(venster, text="Login",
                    command=lambda: verander_label_text(hello_world_label, gebruikers_input.get()))
    # gebruikers_input = Entry(venster, bd=1)




    hello_world_label.place(relx=0.5, rely=0.3, anchor="center")
    label2.place(relx=0.5, rely=0.425, anchor="center")
    gebruikers_input.place(relx=0.5, rely=0.45, anchor="center")
    button.place(relx=0.5, rely=0.5, anchor="center")

def print_naar_console():
    print("De button is geklikt")

def verander_label_text(label, tekst):
    label["text"] = tekst
