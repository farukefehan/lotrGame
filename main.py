from tkinter import Tk, Label
from PIL import Image, ImageTk
from Splash_screen import make_splash_screen


def kill_all_children(venster):
    for widget in venster.winfo_children():
        widget.destroy()


def generate_background(root):
    original_image = Image.open(r"Images/background.png")
    resized_image = original_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(resized_image)
    background = Label(root, image=background_image)
    background.image = background_image
    background.place(x=0, y=0)


def main():
    root = Tk()
    root.title("Boromir")
    root.geometry("1920x1080")
    make_splash_screen(root)

    root.mainloop()


if __name__ == '__main__':
    main()
