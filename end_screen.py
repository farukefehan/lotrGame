from PIL import Image, ImageTk
from tkinter import Label


def clear_page(venster):
    from main import kill_all_children
    kill_all_children(venster)


def goto_splash_screen(venster):
    from main import make_splash_screen
    make_splash_screen(venster)


def make_home_button(venster):
    home_button_image_proto = Image.open(r"images/home_button.png")
    home_button_image_proto = home_button_image_proto.resize((200, 200), Image.LANCZOS)
    home_button_image = ImageTk.PhotoImage(home_button_image_proto)

    home_button = Label(venster, image=home_button_image, compound="bottom", bg="#603000", fg="white")
    home_button.image = home_button_image
    home_button.bind("<Button-1>", lambda click_event: goto_splash_screen(venster))
    home_button.place(relx=0.5, rely=0.8, anchor="center")


def print_adventure_result(venster, image, deathmessage):
    end_image = Image.open(image)
    original_image = end_image.resize((1200, 400), Image.LANCZOS)
    voorbeeld_image = ImageTk.PhotoImage(original_image)

    start_button = Label(venster, text=deathmessage, image=voorbeeld_image, compound="top",
                         bg="#603000", fg="white", font=('castellar', 25))
    start_button.image = voorbeeld_image
    start_button.place(relx=0.5, rely=0.3, anchor="center")
    make_home_button(venster)


def make_end_screen_dead(venster, deathmessage):
    clear_page(venster)
    image_for_result_path = r"images/mission_failed_screen.png"
    print_adventure_result(venster, image_for_result_path, deathmessage)


def make_end_screen_success(venster, deathmessage):
    clear_page(venster)
    image_for_result_path = r"images/the_end.png"
    print_adventure_result(venster, image_for_result_path, deathmessage)
