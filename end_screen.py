from PIL import Image, ImageTk
from tkinter import Label


def clear_page(venster):
    from main import kill_all_children
    kill_all_children(venster)


def goto_splash_screen(venster):
    from main import make_splash_screen
    make_splash_screen(venster)


def print_adventure_result(venster, image):
    end_image = Image.open(image)
    original_image = end_image.resize((1200, 400), Image.LANCZOS)
    voorbeeld_image = ImageTk.PhotoImage(original_image)

    start_button = Label(venster, image=voorbeeld_image, compound="bottom", bg="#603000", fg="white")
    start_button.image = voorbeeld_image
    start_button.place(relx=0.5, rely=0.3, anchor="center")
    make_home_button(venster)


def make_home_button(venster):
    home_button_image_proto = Image.open(r"images/home_button.png")
    home_button_image_proto = home_button_image_proto.resize((200, 200), Image.LANCZOS)
    home_button_image = ImageTk.PhotoImage(home_button_image_proto)

    end_button2 = Label(venster, image=home_button_image, compound="bottom", bg="#603000", fg="white")
    end_button2.image = home_button_image
    end_button2.bind("<Button-1>", lambda click_event: goto_splash_screen(venster))
    end_button2.place(relx=0.5, rely=0.7, anchor="center")


def make_end_screen_dead(venster):
    clear_page(venster)
    image_for_result_path = r"images/you_died.png"
    print_adventure_result(venster, image_for_result_path)


def make_end_screen_success(venster):
    clear_page(venster)
    image_for_result_path = r"images/the_end.png"
    print_adventure_result(venster, image_for_result_path)
