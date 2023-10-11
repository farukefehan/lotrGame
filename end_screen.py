from PIL import Image, ImageTk
from tkinter import Label


def goto_splash_screen(venster):
    from Splash_screen import make_splash_screen
    make_splash_screen(venster)

def make_end_screen(venster, player_has_died):
    from main import kill_all_children
    kill_all_children(venster)

    if player_has_died:
        negative_end_image = Image.open(r"Images/you_died.png")
        original_image_negative = negative_end_image.resize((1200, 400), Image.LANCZOS)
        voorbeeld_image = ImageTk.PhotoImage(original_image_negative)

        start_button = Label(venster, image=voorbeeld_image, compound="bottom")
        start_button.image = voorbeeld_image
        start_button.place(relx=0.5, rely=0.3, anchor="center")
    else:
        positive_end_image = Image.open(r"Images/the_end.png")
        original_image_positive = positive_end_image.resize((1200, 400), Image.LANCZOS)
        voorbeeld_image = ImageTk.PhotoImage(original_image_positive)

        start_button = Label(venster, image=voorbeeld_image, compound="bottom")
        start_button.image = voorbeeld_image
        start_button.place(relx=0.5, rely=0.3, anchor="center")

    original_image2 = Image.open(r"Images/home_button.png")
    original_image2 = original_image2.resize((200, 200), Image.LANCZOS)
    voorbeeld_image2 = ImageTk.PhotoImage(original_image2)

    start_button2 = Label(venster, image=voorbeeld_image2, compound="bottom")
    start_button2.image = voorbeeld_image2
    start_button2.bind("<Button-1>", lambda click_event: goto_splash_screen(venster))
    start_button2.place(relx=0.5, rely=0.7, anchor="center")


