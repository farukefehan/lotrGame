from tkinter import Tk, Label
from splash_screen import make_splash_screen
from PIL import Image, ImageTk
from read_adventure import read_adventure
from paths_screen import start_adventure


def kill_all_children(venster):
    for widget in venster.winfo_children():
        widget.destroy()
    generate_background(venster)


def generate_background(zone):
    original_image = Image.open(r"images/background.png")
    resized_image = original_image.resize((zone.winfo_screenwidth(), zone.winfo_screenheight()), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(resized_image)

    background = Label(zone, image=background_image)
    background.image = background_image
    background.place(x=0, y=0)


def main():
    root = Tk()
    root.geometry("1920x1080")
    root.title("Boromir")
    root.state('zoomed')
    root.winfo_screenheight()
    root.winfo_height()
    generate_background(root)
    make_splash_screen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
